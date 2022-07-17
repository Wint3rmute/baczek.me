#!/bin/bash
set -Eeuo pipefail

CLONE_LOCATION="website"

while true; do
  rm -rf "$CLONE_LOCATION"
  git clone "$REPO_URL" "$CLONE_LOCATION" --depth=1
  cd "$CLONE_LOCATION"

  python related_posts_generator.py
  dot -Tsvg generated/connections.dot > generated/connections.svg
  zola build

  mv public html
  rm -rf /usr/share/nginx/html
  mv html /usr/share/nginx/html
  echo "/usr/share/nginx/html updated"

  echo "sleeping.."
  sleep 360000
done

