from dataclasses import dataclass


@dataclass
class ChatMessage:
    """DTO for a chat message"""

    sender: str  #: The sender of the message
    receiver: str  #: The receiver of the message
    body: str  #: The body of the message
