from fastapi import APIRouter
from pydantic import BaseModel

from agent import agent

router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    history: list = []


@router.post("/chat")
def chat(data: ChatRequest):

    messages = data.history.copy()

    messages.append(
        {
            "role": "user",
            "content": data.message
        }
    )

    response = agent.invoke(
        {
            "messages": messages
        }
    )

    assistant_message = ""

    if isinstance(response, dict):

        msgs = response.get("messages", [])

        if msgs:
            assistant_message = msgs[-1].content

    else:
        assistant_message = str(response)

    return {
        "response": assistant_message
    }