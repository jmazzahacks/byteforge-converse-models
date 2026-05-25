from dataclasses import dataclass
from typing import Optional


@dataclass
class Session:
    """
    A short-lived handshake session that the frontend uses to bootstrap a chat.

    Auth itself is handled by the consuming app; this session carries the
    already-validated user identifier plus a conversation pointer.

    `created_at` and `expires_at` are unix timestamps (epoch seconds).
    """
    id: str
    user_id: str
    conversation_id: Optional[str]
    created_at: int
    expires_at: int

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "conversation_id": self.conversation_id,
            "created_at": self.created_at,
            "expires_at": self.expires_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Session":
        if "id" not in data:
            raise ValueError("id is required")
        if "user_id" not in data:
            raise ValueError("user_id is required")
        if "created_at" not in data:
            raise ValueError("created_at is required")
        if "expires_at" not in data:
            raise ValueError("expires_at is required")

        return cls(
            id=str(data["id"]),
            user_id=str(data["user_id"]),
            conversation_id=str(data["conversation_id"]) if data.get("conversation_id") else None,
            created_at=int(data["created_at"]),
            expires_at=int(data["expires_at"]),
        )
