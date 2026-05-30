from dataclasses import dataclass
from typing import Optional


@dataclass
class ConversationCreate:
    """
    Input payload for creating a conversation.

    Distinct from `Conversation` because the server owns `id`, `created_at`,
    and `updated_at`. The consuming app supplies `user_id` and `title`, plus
    optional per-conversation LLM config (`model`, `system_prompt`,
    `response_schema`, `tools`).
    """
    user_id: str
    title: str
    model: Optional[str] = None
    system_prompt: Optional[str] = None
    response_schema: Optional[dict] = None
    tools: Optional[list] = None

    def to_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "title": self.title,
            "model": self.model,
            "system_prompt": self.system_prompt,
            "response_schema": self.response_schema,
            "tools": self.tools,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "ConversationCreate":
        if not data.get("user_id"):
            raise ValueError("user_id is required")
        if not data.get("title"):
            raise ValueError("title is required")

        response_schema = data.get("response_schema")
        if response_schema is not None and not isinstance(response_schema, dict):
            raise ValueError("response_schema must be a JSON object")

        tools = data.get("tools")
        if tools is not None and not isinstance(tools, list):
            raise ValueError("tools must be a JSON array")

        return cls(
            user_id=str(data["user_id"]),
            title=str(data["title"]),
            model=str(data["model"]) if data.get("model") else None,
            system_prompt=str(data["system_prompt"]) if data.get("system_prompt") else None,
            response_schema=response_schema,
            tools=tools,
        )
