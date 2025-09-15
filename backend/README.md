# Backend API

This is the Rust backend API for baczek.me, built with Axum and integrated with Utoipa for automatic OpenAPI specification generation.

## Features

- RESTful API endpoints for user management
- Automatic OpenAPI 3.0 specification generation using Utoipa
- Interactive API documentation via Swagger UI
- Health check endpoint
- CORS support for cross-origin requests

## Getting Started

### Prerequisites

- Rust 1.70+ (https://rustup.rs/)

### Installation

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   cargo build
   ```

3. Run the server:
   ```bash
   cargo run
   ```

The server will start on `http://localhost:3000`.

### API Documentation

Once the server is running, you can access:

- **Swagger UI**: http://localhost:3000/swagger-ui
  - Interactive API documentation with the ability to test endpoints
- **OpenAPI JSON Spec**: http://localhost:3000/openapi.json
  - Raw OpenAPI 3.0 specification in JSON format

## API Endpoints

### Users

- `GET /api/users` - Get all users
- `GET /api/users/{id}` - Get user by ID
- `POST /api/users` - Create a new user
- `DELETE /api/users/{id}` - Delete user by ID

### Health Check

- `GET /health` - Health check endpoint

## Data Models

The API uses the following data models, all automatically documented in the OpenAPI spec:

- `User` - User entity with id, username, and email
- `CreateUserRequest` - Request payload for creating users
- `SuccessResponse` - Standard success response
- `ErrorResponse` - Standard error response

## Development

### Adding New Endpoints

1. Add the handler function to `src/handlers.rs` with proper `#[utoipa::path(...)]` annotations
2. Add the data models to `src/models.rs` with `#[derive(utoipa::ToSchema)]`
3. Update the `#[derive(OpenApi)]` macro in `src/main.rs` to include new paths and schemas
4. Add the route to the router in `main.rs`

### Example Handler

```rust
#[utoipa::path(
    get,
    path = "/api/example",
    responses(
        (status = 200, description = "Success", body = ExampleResponse),
    ),
    tag = "example"
)]
pub async fn example_handler() -> Json<ExampleResponse> {
    // Implementation
}
```

The OpenAPI documentation will be automatically updated when you restart the server.

## License

This project is part of the baczek.me website.