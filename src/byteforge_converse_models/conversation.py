from dataclasses import dataclass
from typing import Optional


@dataclass
class Conversation:
    """
    A single conversation between a user and the LLM.

    `created_at` and `updated_at` are unix timestamps (epoch seconds).
    `user_id` is whatever identifier the consuming app provides; this library
    does not own auth.
    """
    id: str
    user_id: str
    title: str
    created_at: int
    updated_at: Optional[int] = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Conversation":
        if "id" not in data:
            raise ValueError("id is required")
        if "user_id" not in data:
            raise ValueError("user_id is required")
        if "title" not in data:
            raise ValueError("title is required")
        if "created_at" not in data:
            raise ValueError("created_at is required")

        return cls(
            id=str(data["id"]),
            user_id=str(data["user_id"]),
            title=str(data["title"]),
            created_at=int(data["created_at"]),
            updated_at=int(data["updated_at"]) if data.get("updated_at") else None,
        )
