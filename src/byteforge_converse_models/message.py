from dataclasses import dataclass
from typing import Optional, List


VALID_ROLES = {"user", "assistant", "system", "tool"}


@dataclass
class Message:
    """
    A single message within a conversation.

    `created_at` is a unix timestamp (epoch seconds).
    `role` is one of: user, assistant, system, tool.

    `tool_calls` (when set, only on `assistant` rows) is the opaque list of
    OpenAI/OpenRouter tool-call dicts the model emitted on this turn. Storing
    them lets the next turn's history replay carry the assistant's tool-call
    request, which is required by the OpenAI tool-calling protocol when the
    caller later feeds a tool result back as a `tool` row.

    `tool_call_id` (only on `tool` rows) is the id of the assistant tool_call
    this row is responding to. Required by OpenAI when role='tool'.
    """
    id: str
    conversation_id: str
    role: str
    content: str
    created_at: int
    token_count: Optional[int] = None
    tool_calls: Optional[List[dict]] = None
    tool_call_id: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "conversation_id": self.conversation_id,
            "role": self.role,
            "content": self.content,
            "created_at": self.created_at,
            "token_count": self.token_count,
            "tool_calls": self.tool_calls,
            "tool_call_id": self.tool_call_id,
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

        tool_calls = data.get("tool_calls")
        if tool_calls is not None and not isinstance(tool_calls, list):
            raise ValueError("tool_calls must be a JSON array")

        return cls(
            id=str(data["id"]),
            conversation_id=str(data["conversation_id"]),
            role=role,
            content=str(data["content"]),
            created_at=int(data["created_at"]),
            token_count=int(data["token_count"]) if data.get("token_count") is not None else None,
            tool_calls=tool_calls,
            tool_call_id=str(data["tool_call_id"]) if data.get("tool_call_id") else None,
        )
