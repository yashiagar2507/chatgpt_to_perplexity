# 🔁 ChatGPT to Perplexity Bridge

This tool helps you take a conversation from ChatGPT and continue it seamlessly in [Perplexity AI](https://www.perplexity.ai), so you can pick up where you left off — even across platforms.

---

## 🚀 What It Does

- ✅ Lets you export all your past ChatGPT chats into an Excel file
- ✅ You select a chat (by title or row number)
- ✅ The script pastes that conversation into Perplexity.ai automatically
- ✅ It appends this line to simulate chat continuation:

> _“This is the chat I had with ChatGPT, and now give me response for next messages that I’ll send.”_

- 🗨️ After that, you can keep chatting manually with Perplexity

---

## 🧰 Requirements

- Python 3.8+
- Google Chrome + ChromeDriver
- Install dependencies:
```bash
pip install selenium pandas openpyxl
## How to use it

1. Export your ChatGPT chats
Go to ChatGPT → Settings → Data Controls → Export
You'll get a .zip via email. Extract it and find the conversations.json file.

Place it in this project folder.

2. Extract chats to Excel
python extract_chats_to_excel.py

3. Open the Excel file and choose a row

4. Edit send_selected_chat_to_perplexity.py
Set the row number you want to send:
row_number = 1

5. Run the script to send that chat
python send_selected_chat_to_perplexity.py

💡 This will:

Open Perplexity in Chrome
Paste your selected ChatGPT conversation
Append the custom instruction line

You can copy the prompt from there to perplexity and starr chatting!






