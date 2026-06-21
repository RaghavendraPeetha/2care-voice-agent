from fastapi import FastAPI

from app.chat_api import router as chat_router

app = FastAPI(
    title="2Care Voice AI",
    description="DeepAgents Hospital Receptionist",
    version="1.0.0"
)

app.include_router(chat_router)


@app.get("/")
def home():
    return {
        "message": "2Care Voice AI Running"
    }