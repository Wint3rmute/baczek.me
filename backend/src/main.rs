mod handlers;
mod models;

use axum::{
    routing::{delete, get, post},
    Router,
};
use tower_http::cors::CorsLayer;
use utoipa::OpenApi;
use utoipa_swagger_ui::SwaggerUi;

use handlers::{create_user, delete_user, get_user_by_id, get_users, health_check};
use models::{CreateUserRequest, ErrorResponse, SuccessResponse, User};

/// API Documentation struct that aggregates all endpoints and schemas
#[derive(OpenApi)]
#[openapi(
    paths(
        handlers::get_users,
        handlers::get_user_by_id,
        handlers::create_user,
        handlers::delete_user,
        handlers::health_check,
    ),
    components(
        schemas(User, CreateUserRequest, SuccessResponse, ErrorResponse)
    ),
    tags(
        (name = "users", description = "User management endpoints"),
        (name = "health", description = "Health check endpoints")
    ),
    info(
        title = "Baczek.me API",
        version = "1.0.0",
        description = "A REST API for the baczek.me backend service",
        contact(
            name = "API Support",
            url = "https://github.com/Wint3rmute/baczek.me",
            email = "mateusz.baczek1998@gmail.com"
        )
    ),
    servers(
        (url = "http://localhost:3000", description = "Local development server"),
        (url = "https://api.baczek.me", description = "Production server")
    )
)]
pub struct ApiDoc;

#[tokio::main]
async fn main() {
    // Initialize tracing
    tracing_subscriber::fmt::init();

    // Build our application with routes
    let app = Router::new()
        // API routes
        .route("/api/users", get(get_users))
        .route("/api/users", post(create_user))
        .route("/api/users/:id", get(get_user_by_id))
        .route("/api/users/:id", delete(delete_user))
        .route("/health", get(health_check))
        // OpenAPI JSON spec endpoint
        .route("/openapi.json", get(openapi_json))
        // Swagger UI (this will create its own /openapi.json endpoint)
        .merge(SwaggerUi::new("/swagger-ui").url("/api-docs/openapi.json", ApiDoc::openapi()))
        // CORS layer for cross-origin requests
        .layer(CorsLayer::permissive());

    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000")
        .await
        .unwrap();

    println!("🚀 Server starting on http://0.0.0.0:3000");
    println!("📖 API documentation available at: http://0.0.0.0:3000/swagger-ui");
    println!("📄 OpenAPI spec available at: http://0.0.0.0:3000/openapi.json");

    axum::serve(listener, app).await.unwrap();
}

/// Serve the OpenAPI specification as JSON
async fn openapi_json() -> axum::response::Json<utoipa::openapi::OpenApi> {
    axum::response::Json(ApiDoc::openapi())
}