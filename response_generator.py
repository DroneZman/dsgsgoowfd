import openai
from context_manager import get_context, update_context

openai.api_key = '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'


def generate_response(user_data: dict, question: str) -> str:
    chat_context = get_context(user_data)
    messages = []
    for part in chat_context.split("\n"):
        if ": " not in part:
            continue  # skip this line
        role, content = part.split(": ", 1)  # use 1 as the maxsplit argument
        role = "assistant" if role.lower() == "bot" else role.lower()
        messages.append({"role": role, "content": content})

    messages.append({"role": "user", "content": question})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    answer = response['choices'][0]['message']['content']
    update_context(user_data, question, answer)
    return answer
