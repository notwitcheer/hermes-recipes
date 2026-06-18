#!/usr/bin/env bash
# secure-box.sh - first-boot hardening for a fresh Ubuntu 24.04 VPS, before installing Hermes Agent.
#
# what it does, as root on a fresh box:
#   - apt update + upgrade
#   - adds a 2G swapfile (a cheap VPS often ships with none; the Hermes install can spike memory)
#   - creates a non-root sudo user with your ssh key
#   - locks ssh to key-only: no passwords, no root login
#   - turns on a minimal firewall (ssh only)
#
# usage:
#   1. edit NEW_USER and SSH_PUBKEY below
#   2. copy this to the box and run as root:  bash secure-box.sh
#   3. IMPORTANT: in a SEPARATE terminal, confirm you can log in as the new user
#      before you close the root session:     ssh <NEW_USER>@<your-vps-ip>
#
# tested on: Hetzner CX23 (x86, 2 vCPU, 4GB), Ubuntu 24.04.4 LTS, 2026-06-18.

set -euo pipefail

# ---- edit these two ----
NEW_USER="hermes"
SSH_PUBKEY="ssh-ed25519 AAAA...replace-with-your-own-public-key... you@yourmachine"
# ------------------------

if [ "$(id -u)" -ne 0 ]; then
  echo "run this as root on a fresh box"; exit 1
fi
if [[ "$SSH_PUBKEY" == *"replace-with-your-own-public-key"* ]]; then
  echo "edit SSH_PUBKEY first: paste your own public key (cat ~/.ssh/id_ed25519.pub on your machine)"; exit 1
fi

export DEBIAN_FRONTEND=noninteractive NEEDRESTART_MODE=a

echo "==> apt update + upgrade"
apt-get update -qq
apt-get upgrade -y -qq

echo "==> 2G swap"
if ! swapon --show | grep -q '/swapfile'; then
  fallocate -l 2G /swapfile
  chmod 600 /swapfile
  mkswap /swapfile >/dev/null
  swapon /swapfile
  echo '/swapfile none swap sw 0 0' >> /etc/fstab
fi
grep -q '^vm.swappiness' /etc/sysctl.conf || echo 'vm.swappiness=10' >> /etc/sysctl.conf
sysctl -p >/dev/null

echo "==> non-root user '$NEW_USER' with sudo and your ssh key"
id "$NEW_USER" &>/dev/null || useradd -m -s /bin/bash "$NEW_USER"
usermod -aG sudo "$NEW_USER"
# passwordless sudo so the box can run unattended maintenance. if you do not want that,
# delete the next three lines and set a password instead: passwd "$NEW_USER"
echo "$NEW_USER ALL=(ALL) NOPASSWD:ALL" > "/etc/sudoers.d/90-$NEW_USER"
chmod 440 "/etc/sudoers.d/90-$NEW_USER"
visudo -cf "/etc/sudoers.d/90-$NEW_USER"
install -d -m 700 -o "$NEW_USER" -g "$NEW_USER" "/home/$NEW_USER/.ssh"
echo "$SSH_PUBKEY" > "/home/$NEW_USER/.ssh/authorized_keys"
chown "$NEW_USER:$NEW_USER" "/home/$NEW_USER/.ssh/authorized_keys"
chmod 600 "/home/$NEW_USER/.ssh/authorized_keys"

echo "==> lock ssh to key-only, no root login"
# this image can ship with password auth ON even when you added a key at create time, so set it explicitly
cat > /etc/ssh/sshd_config.d/00-hardening.conf <<'EOF'
PubkeyAuthentication yes
PasswordAuthentication no
KbdInteractiveAuthentication no
PermitRootLogin no
EOF
sshd -t
systemctl reload ssh

echo "==> firewall: ssh only (Telegram uses outbound long-polling, so no inbound port is needed)"
ufw allow OpenSSH
ufw --force enable

echo
echo "done. before closing this root session, open a NEW terminal and confirm:"
echo "    ssh ${NEW_USER}@<your-vps-ip>"
