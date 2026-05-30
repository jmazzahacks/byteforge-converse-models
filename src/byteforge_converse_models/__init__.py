"""
Shared data models for ByteforgeConverse — conversations, messages, turns, and sessions.
"""

from .conversation import Conversation
from .conversation_create import ConversationCreate
from .message import Message, VALID_ROLES
from .session import Session
from .tool_call import ToolCall
from .chat_turn import ChatTurn

__version__ = "0.3.0"

__all__ = [
    "Conversation",
    "ConversationCreate",
    "Message",
    "Session",
    "ToolCall",
    "ChatTurn",
    "VALID_ROLES",
]
