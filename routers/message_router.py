# routers/message_router.py
from fastapi import APIRouter
from controllers.message_controller import get_hello_world
from models.message_model import Message

router = APIRouter()

@router.get("/", response_model=Message)
def read_root():
    return get_hello_world()
