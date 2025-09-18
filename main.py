# main.py
from fastapi import FastAPI
from routers import message_router

app = FastAPI()

# Attach your router
app.include_router(message_router.router)
