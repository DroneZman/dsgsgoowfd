def get_context(user_data: dict) -> str:
    if not user_data.get('context_on', True):
        return ""
    messages = user_data.get('messages', [])
    context = "\n".join(messages[-4:])  # get last 4 messages
    if len(context) > 3000:
        context = context[-3000:]  # ensure context is not larger than 3000 characters
    return context

def update_context(user_data: dict, question: str, answer: str) -> None:
    messages = user_data.get('messages', [])
    messages.append(f"User: {question}")
    messages.append(f"Assistant: {answer}")
    user_data['messages'] = messages

def toggle_context(user_data: dict) -> None:
    user_data['context_on'] = not user_data.get('context_on', True)

def reset_context(user_data: dict) -> None:
    user_data['messages'] = []
