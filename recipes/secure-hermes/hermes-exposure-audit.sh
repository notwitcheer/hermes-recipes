#!/usr/bin/env bash
# hermes-exposure-audit.sh: self-check for a self-hosted Hermes Agent's network + secret posture.
# read-only: it inspects, never changes anything. run it on the box that runs Hermes Agent.
# checks: (1) what Hermes listens on (expect: nothing off-loopback), (2) .env perms (expect 600),
#         (3) .env not tracked by git, (4) any forced 0.0.0.0 / insecure dashboard|API bind,
#         (5) a command allowlist is set, (6) a recent ~/.hermes backup exists.
# exit 0 if clean, 1 if any WARN. part of the secure-hermes recipe.
# tested on Hermes Agent v0.17.0 (Ubuntu 24.04 x86 + macOS).
set -uo pipefail
HHOME="${HERMES_HOME:-$HOME/.hermes}"
warn=0
ok(){  printf '  ok   %s\n' "$*"; }
bad(){ printf '  WARN %s\n' "$*"; warn=1; }

echo "== hermes exposure audit =="
echo "hermes home: $HHOME"

# 1. listeners: is anything bound OFF loopback?
echo; echo "[1] inbound listeners (expect: ssh only, nothing Hermes)"
if command -v ss >/dev/null 2>&1; then
  listen=$(ss -tlnH 2>/dev/null | awk '{print $4}')
elif command -v lsof >/dev/null 2>&1; then
  listen=$(lsof -nP -iTCP -sTCP:LISTEN 2>/dev/null | awk 'NR>1{print $9}')
else
  bad "neither ss nor lsof found; cannot check listeners"; listen=""
fi
# strip loopback (any 127.x, ::1, %lo iface) and ssh (:22); anything left is an unexpected inbound listener
nonloop=$(printf '%s\n' "$listen" | grep -E '[0-9]' | grep -vE '127\.|::1|%lo' | grep -vE ':22$' || true)
if [ -z "$nonloop" ]; then ok "nothing listening off-loopback except ssh (gateway is outbound-only)"
else bad "unexpected off-loopback listeners (not ssh): review each:"; printf '%s\n' "$nonloop" | sed 's/^/         /'; fi
if printf '%s\n' "$listen" | grep -qE '(0\.0\.0\.0|\*):(9119|8642)'; then
  bad "dashboard(9119) or API(8642) bound to 0.0.0.0: exposed to the network"
else ok "dashboard(9119)/API(8642) not bound to 0.0.0.0"; fi

# 2. .env perms
echo; echo "[2] .env permissions (expect 600)"
if [ -f "$HHOME/.env" ]; then
  perm=$(stat -c '%a' "$HHOME/.env" 2>/dev/null || stat -f '%Lp' "$HHOME/.env" 2>/dev/null)
  [ "$perm" = "600" ] && ok ".env is 600 (owner-only)" || bad ".env is $perm (run: chmod 600 $HHOME/.env)"
else ok "no .env at $HHOME/.env"; fi

# 3. .env not tracked by git
echo; echo "[3] .env not committed to git"
if [ -d "$HHOME/.git" ] && git -C "$HHOME" ls-files --error-unmatch .env >/dev/null 2>&1; then
  bad ".env is TRACKED by git in $HHOME: untrack and gitignore it now"
else ok ".env not tracked by git here"; fi

# 4. forced non-loopback / insecure binds in the environment
echo; echo "[4] forced 0.0.0.0 / insecure dashboard|API binds"
if env | grep -qiE 'HERMES_DASHBOARD_HOST=0\.0\.0\.0|API_SERVER_HOST=0\.0\.0\.0|HERMES_DASHBOARD_INSECURE=(1|true|yes)'; then
  bad "an env var forces a non-loopback dashboard/API bind or disables the dashboard auth gate"
else ok "no 0.0.0.0 / insecure dashboard|API override in the environment"; fi

# 5. command allowlist set
echo; echo "[5] command allowlist"
cfg="$HHOME/config.yaml"
if [ -f "$cfg" ] && awk '/^[[:space:]]*command_allowlist:/{f=1;next} f&&/[^[:space:]]/{print;exit}' "$cfg" | grep -q '[^[:space:]]'; then
  ok "command_allowlist is set in config.yaml"
else bad "no command_allowlist in config.yaml: the agent's shell tool can run any command"; fi

# 6. recent ~/.hermes backup
echo; echo "[6] recent ~/.hermes backup"
bdir="${HERMES_BACKUP_DIR:-$HOME/hermes-backups}"
recent=$(find "$bdir" -name '*.tar.*' -mtime -14 2>/dev/null | head -1 || true)
[ -n "$recent" ] && ok "a backup <14d old exists: $recent" || bad "no recent backup in $bdir (see the backup step)"

echo
if [ "$warn" -eq 0 ]; then echo "== clean =="; exit 0; else echo "== WARN: review the flags above =="; exit 1; fi
