# controllers/message_controller.py
from models.message_model import Message

def get_hello_world() -> Message:
    return Message(message="Hello, World!")
