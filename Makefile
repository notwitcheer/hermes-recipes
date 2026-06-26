# hermes-recipes site build
# recipes/ and CHANGELOG.md stay the source of truth; the site is generated.
# `stage` copies them under docs/ (gitignored) so mkdocs can render them
# without polluting the repo files with site front matter.

.PHONY: stage serve build clean

stage:
	rm -rf docs/recipes docs/changelog.md
	cp -r recipes docs/recipes
	cp CHANGELOG.md docs/changelog.md

serve: stage
	mkdocs serve

build: stage
	mkdocs build --strict

clean:
	rm -rf docs/recipes docs/changelog.md site
