from dataclasses import dataclass


@dataclass
class ToolCall:
    """
    A single tool invocation requested by the model.

    Mirrors the standard OpenAI/OpenRouter tool-call shape. Converse stores
    nothing about tool calls itself — these objects are produced by
    `ChatService` for the relay turn and consumed by the caller, which
    executes the tool out-of-band.

    `arguments` is the raw JSON string emitted by the model. We do not parse
    or validate it; the caller decides how to interpret it.
    """
    id: str
    name: str
    arguments: str

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "arguments": self.arguments,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "ToolCall":
        if "id" not in data:
            raise ValueError("id is required")
        if "name" not in data:
            raise ValueError("name is required")
        if "arguments" not in data:
            raise ValueError("arguments is required")

        return cls(
            id=str(data["id"]),
            name=str(data["name"]),
            arguments=str(data["arguments"]),
        )
