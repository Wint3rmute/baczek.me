# [My Personal Website](https://baczek.me)

You should make one for yourself too :)

## Building

I'm using [Zola](https://www.getzola.org/) + some extra scripts to build my
[site map and related pages](https://baczek.me/map).

If you have [Poetry](https://python-poetry.org/) installed, simply run `poetry
install` and `poetry run python -m exocortex`, then `zola serve` or `zola
build`.

If you prefer to keep everything isolated, use the [`Dockerfile`](./Dockerfile)
to build an image which can then run the commands above. Refer to the [CI build
job definition](./.github/workflows/zola.yml) for details.

## Backend API

This repository also includes a Rust backend API with automatic OpenAPI documentation generation:

### Getting Started with the API

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Run the server:
   ```bash
   cargo run
   ```

3. Access the API documentation:
   - **Swagger UI**: http://localhost:3000/swagger-ui
   - **OpenAPI Spec**: http://localhost:3000/openapi.json

For detailed backend documentation, see [backend/README.md](./backend/README.md).
