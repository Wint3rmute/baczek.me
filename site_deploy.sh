#!/bin/bash
set -Eeuo pipefail

CLONE_LOCATION="website"

rm -rf "$CLONE_LOCATION"
git clone "$REPO_URL" "$CLONE_LOCATION" --depth=1
cd "$CLONE_LOCATION"

python -m related_generator
zola build

mv public html
rm -rf /usr/share/nginx/html
mv html /usr/share/nginx/html
echo "/usr/share/nginx/html updated"

