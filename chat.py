from datetime import datetime

from agent import agent


TODAY = datetime.now().strftime("%Y-%m-%d")

print("\n2Care Voice Receptionist Agent")
print(f"Today's Date: {TODAY}")
print("Type 'exit' to quit.\n")


conversation = [
    {
        "role": "system",
        "content": f"""
Current date: {TODAY}

Date Rules:

- If the patient says "today", use {TODAY}.
- If the patient says "tomorrow", calculate the next calendar day.
- If the patient says "next week", calculate the proper date.
- Never invent dates.
- Always use YYYY-MM-DD format internally.
"""
    }
]


while True:

    user_input = input("User: ")

    if user_input.lower() == "exit":
        break

    conversation.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    try:

        response = agent.invoke(
            {
                "messages": conversation
            }
        )

        print("\nAgent:")

        if isinstance(response, dict):

            messages = response.get("messages", [])

            if messages:

                assistant_message = messages[-1].content

                print(assistant_message)

                conversation.append(
                    {
                        "role": "assistant",
                        "content": assistant_message
                    }
                )

            else:
                print(response)

        else:
            print(response)

    except Exception as e:

        print("\nERROR:")
        print(str(e))

    print()