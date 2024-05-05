set -Eeuo pipefail

poetry run black .
poetry run isort .
poetry run ruff --fix .
