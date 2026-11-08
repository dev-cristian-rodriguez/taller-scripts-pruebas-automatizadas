"""JSON Schema (Draft 7) del recurso post de JSONPlaceholder."""
POST_SCHEMA = {
    "type": "object",
    "required": ["userId", "id", "title", "body"],
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string", "minLength": 1},
        "body": {"type": "string"},
    },
}
