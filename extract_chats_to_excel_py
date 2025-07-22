import json
import pandas as pd

def extract_to_excel(json_file='conversations.json', output_excel='chat_history.xlsx'):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    rows = []
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
        if messages:
            rows.append({
                "Title": title,
                "Conversation": "\n".join(messages)
            })

    df = pd.DataFrame(rows)
    df.to_excel(output_excel, index=False)
    print(f"✅ Exported {len(df)} conversations to {output_excel}")

# Run the function
extract_to_excel()
