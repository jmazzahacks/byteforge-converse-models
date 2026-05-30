from dataclasses import dataclass
from typing import Optional, List

from .message import Message
from .tool_call import ToolCall


@dataclass
class ChatTurn:
    """
    The result of a single chat turn.

    `message` is the persisted assistant Message. It is always present — its
    `content` may be the empty string for a turn that produced only tool
    calls, or it may carry both narration and tool calls.

    `tool_calls` is the list of tools the model asked the caller to execute.
    None when the turn was a normal reply. The caller executes the tools
    out-of-band (Converse never executes a tool itself) and is expected to
    feed each result back as a `tool` role message via the messages endpoint
    before the next chat turn — `tool_call_id` on each result must match a
    ToolCall.id from this turn.
    """
    message: Message
    tool_calls: Optional[List[ToolCall]] = None

    def to_dict(self) -> dict:
        return {
            "message": self.message.to_dict(),
            "tool_calls": [tc.to_dict() for tc in self.tool_calls] if self.tool_calls is not None else None,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "ChatTurn":
        message_data = data.get("message")
        if not message_data:
            raise ValueError("message is required")

        tool_calls_data = data.get("tool_calls")
        if tool_calls_data is not None and not isinstance(tool_calls_data, list):
            raise ValueError("tool_calls must be a JSON array")

        tool_calls = (
            [ToolCall.from_dict(tc) for tc in tool_calls_data]
            if tool_calls_data is not None
            else None
        )

        return cls(
            message=Message.from_dict(message_data),
            tool_calls=tool_calls,
        )
