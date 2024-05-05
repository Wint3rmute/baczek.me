set -Eeuo pipefail

poetry run python -m exocortex
zola build
