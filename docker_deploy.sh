#!/bin/bash
set -Eeuo pipefail

CLONE_LOCATION="website"

while true; do
  rm -rf "$CLONE_LOCATION"
  git clone "$REPO_URL" "$CLONE_LOCATION" --depth=1
  cd "$CLONE_LOCATION"

  zola build

  mv public html
  rm -rf /usr/share/nginx/html
  mv html /usr/share/nginx/html
  echo "/usr/share/nginx/html updated"

  echo "sleeping.."
  sleep 36000
done

