from dataclasses import dataclass
from typing import Optional


@dataclass
class Conversation:
    """
    A single conversation between a user and the LLM.

    `created_at` and `updated_at` are unix timestamps (epoch seconds).
    `user_id` is whatever identifier the consuming app provides; this library
    does not own auth.

    `model`, `system_prompt`, and `response_schema` are per-conversation LLM
    configuration set by the consuming app. `model` falls back to the backend
    default when None. `system_prompt` encodes the conversation's purpose.
    `response_schema` is a JSON schema for structured-output conversations
    (None for freeform chat).

    `tools` is an opaque list of standard OpenAI/OpenRouter tool definitions.
    Converse forwards them to the model and relays any resulting tool calls
    back to the caller without interpretation.
    """
    id: str
    user_id: str
    title: str
    created_at: int
    updated_at: Optional[int] = None
    model: Optional[str] = None
    system_prompt: Optional[str] = None
    response_schema: Optional[dict] = None
    tools: Optional[list] = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "model": self.model,
            "system_prompt": self.system_prompt,
            "response_schema": self.response_schema,
            "tools": self.tools,
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

        tools = data.get("tools")
        if tools is not None and not isinstance(tools, list):
            raise ValueError("tools must be a JSON array")

        return cls(
            id=str(data["id"]),
            user_id=str(data["user_id"]),
            title=str(data["title"]),
            created_at=int(data["created_at"]),
            updated_at=int(data["updated_at"]) if data.get("updated_at") else None,
            model=str(data["model"]) if data.get("model") else None,
            system_prompt=str(data["system_prompt"]) if data.get("system_prompt") else None,
            response_schema=data.get("response_schema"),
            tools=tools,
        )
