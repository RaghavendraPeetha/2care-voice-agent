from fastapi import APIRouter
from pydantic import BaseModel

from agent import agent

router = APIRouter()

conversation_store = {}


class ChatRequest(BaseModel):
    message: str
    session_id: str


@router.post("/chat")
def chat(data: ChatRequest):

    if data.session_id not in conversation_store:
        conversation_store[data.session_id] = []

    messages = conversation_store[data.session_id]

    messages.append(
        {
            "role": "user",
            "content": data.message
        }
    )

    try:

        response = agent.invoke(
            {
                "messages": messages
            },
            config={
                "thread_id": data.session_id
            }
        )

        assistant_message = ""

        if isinstance(response, dict):

            msgs = response.get(
                "messages",
                []
            )

            for msg in reversed(msgs):

                if hasattr(msg, "content"):

                    if msg.content:

                        assistant_message = str(
                            msg.content
                        )

                        break

        else:
            assistant_message = str(response)

        if not assistant_message:

            assistant_message = (
                "I couldn't complete that request right now."
            )

        messages.append(
            {
                "role": "assistant",
                "content": assistant_message
            }
        )

        return {
            "response": assistant_message
        }

    except Exception as e:

        print(e)

        return {
            "response":
            "I couldn't complete that request right now. Please try again."
        }