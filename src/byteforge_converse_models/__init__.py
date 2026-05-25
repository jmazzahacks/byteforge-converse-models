"""
Shared data models for ByteforgeConverse — conversations, messages, turns, and sessions.
"""

from .conversation import Conversation
from .message import Message, VALID_ROLES
from .session import Session

__version__ = "0.0.1"

__all__ = [
    "Conversation",
    "Message",
    "Session",
    "VALID_ROLES",
]
