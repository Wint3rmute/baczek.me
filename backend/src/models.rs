use serde::{Deserialize, Serialize};
use utoipa::ToSchema;

/// User data model
#[derive(Serialize, Deserialize, ToSchema, Clone)]
pub struct User {
    /// Unique user identifier
    #[schema(example = 1)]
    pub id: u32,
    
    /// User's display name
    #[schema(example = "john_doe")]
    pub username: String,
    
    /// User's email address
    #[schema(example = "john@example.com")]
    pub email: String,
}

/// Request body for creating a new user
#[derive(Deserialize, ToSchema)]
pub struct CreateUserRequest {
    /// User's display name
    #[schema(example = "john_doe")]
    pub username: String,
    
    /// User's email address
    #[schema(example = "john@example.com")]
    pub email: String,
}

/// Response for successful operations
#[derive(Serialize, ToSchema)]
pub struct SuccessResponse {
    /// Success message
    #[schema(example = "Operation completed successfully")]
    pub message: String,
}

/// Error response
#[derive(Serialize, ToSchema)]
pub struct ErrorResponse {
    /// Error message
    #[schema(example = "Something went wrong")]
    pub error: String,
}