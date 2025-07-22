import json

def parse_chat_history(json_file='conversations.json'):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    sessions = []
    for conv in data:
        title = conv.get('title', 'Untitled Chat')
        messages = []

        for msg in conv.get('mapping', {}).values():
            if not isinstance(msg, dict):
                continue
            message = msg.get('message')
            if not message:
                continue
            author = message.get('author', {})
            role = author.get('role')
            parts = message.get('content', {}).get('parts', [])
            if role and parts:
                messages.append(f"{role.upper()}: {parts[0]}")

        text = "\n".join(messages)
        if text.strip():
            sessions.append((title, text))

    return sessions

