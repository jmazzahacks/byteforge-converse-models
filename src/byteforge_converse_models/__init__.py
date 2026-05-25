"""
Shared data models for ByteforgeConverse — conversations, messages, turns, and sessions.
"""

from .conversation import Conversation
from .conversation_create import ConversationCreate
from .message import Message, VALID_ROLES
from .session import Session

__version__ = "0.1.0"

__all__ = [
    "Conversation",
    "ConversationCreate",
    "Message",
    "Session",
    "VALID_ROLES",
]
