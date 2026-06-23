from fastapi import APIRouter
from pydantic import BaseModel

from agent import agent

router = APIRouter()

# Conversation memory by session
conversation_store = {}


class ChatRequest(BaseModel):
    message: str
    session_id: str


@router.post("/chat")
def chat(data: ChatRequest):

    print("\n" + "=" * 60)
    print("SESSION:", data.session_id)
    print("USER MESSAGE:", data.message)
    print("=" * 60)

    # Create conversation if needed
    if data.session_id not in conversation_store:
        conversation_store[data.session_id] = []

        print(f"NEW SESSION CREATED: {data.session_id}")

    messages = conversation_store[data.session_id]

    # Add user message
    messages.append(
        {
            "role": "user",
            "content": data.message
        }
    )

    print("\nCONVERSATION HISTORY:")
    for m in messages:
        print(m)

    try:

        response = agent.invoke(
            {
                "messages": messages
            }
        )

        print("\nAGENT RESPONSE:")
        print(response)

        assistant_message = ""

        if isinstance(response, dict):

            msgs = response.get("messages", [])

            if msgs:

                last_msg = msgs[-1]

                if hasattr(last_msg, "content"):
                    assistant_message = last_msg.content
                else:
                    assistant_message = str(last_msg)

            else:
                assistant_message = (
                    "I couldn't understand the request."
                )

        else:
            assistant_message = str(response)

    except Exception as e:

        print("AGENT ERROR:", str(e))

        assistant_message = (
            "I couldn't complete that request right now."
        )

    # Save assistant response
    messages.append(
        {
            "role": "assistant",
            "content": assistant_message
        }
    )

    print("\nASSISTANT:")
    print(assistant_message)
    print("=" * 60 + "\n")

    return {
        "response": assistant_message
    }