# 🔁 ChatGPT to Perplexity Bridge

This tool helps you take a conversation from ChatGPT and continue it seamlessly in [Perplexity AI](https://www.perplexity.ai), so you can pick up where you left off — even across platforms.

---

## 🚀 What It Does

- ✅ Export all your past ChatGPT chats into an Excel file
- ✅ Choose a chat by row number
- ✅ Paste it automatically into Perplexity.ai
- ✅ Appends this line:

> _"This is the chat I had with ChatGPT, and now give me response for next messages that I’ll send."_

- 🗨️ After that, you can continue chatting manually in Perplexity

---

## 🧰 Requirements

- Python 3.8+
- Chrome + ChromeDriver
- Install dependencies:

## 📦 How to Use It (Step-by-Step)

1. Export your ChatGPT chats
Go to ChatGPT → Settings → Data Controls → Export
Download the .zip from your email
Extract conversations.json and put it in this folder

2. Convert your chats to Excel
```
python extract_chats_to_excel.py
```
This creates chat_history.xlsx with all your titles and conversations.

4. Choose which chat to send
Open chat_history.xlsx
Find the row number of the chat you want

5. Set your row in the script
Edit send_selected_chat_to_perplexity.py:

6. Run the script
```
python send_selected_chat_to_perplexity.py 
```
The script will:
Open Perplexity in Chrome
Paste your selected conversation
Add the follow-up line

You can paste that prompt in perplexity and start chatting there!






