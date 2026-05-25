from dataclasses import dataclass
from typing import Optional


VALID_ROLES = {"user", "assistant", "system", "tool"}


@dataclass
class Message:
    """
    A single message within a conversation.

    `created_at` is a unix timestamp (epoch seconds).
    `role` is one of: user, assistant, system, tool.
    """
    id: str
    conversation_id: str
    role: str
    content: str
    created_at: int
    token_count: Optional[int] = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "conversation_id": self.conversation_id,
            "role": self.role,
            "content": self.content,
            "created_at": self.created_at,
            "token_count": self.token_count,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Message":
        if "id" not in data:
            raise ValueError("id is required")
        if "conversation_id" not in data:
            raise ValueError("conversation_id is required")
        if "role" not in data:
            raise ValueError("role is required")
        if "content" not in data:
            raise ValueError("content is required")
        if "created_at" not in data:
            raise ValueError("created_at is required")

        role = str(data["role"])
        if role not in VALID_ROLES:
            raise ValueError(f"role must be one of {sorted(VALID_ROLES)}, got {role!r}")

        return cls(
            id=str(data["id"]),
            conversation_id=str(data["conversation_id"]),
            role=role,
            content=str(data["content"]),
            created_at=int(data["created_at"]),
            token_count=int(data["token_count"]) if data.get("token_count") is not None else None,
        )
