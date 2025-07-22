# ChatGPT to Perplexity Automation (macOS)

## 🛠 Requirements
- Python 3.8+
- Google Chrome
- ChromeDriver (installed and added to PATH)

## 📦 Setup
```bash
pip install -r requirements.txt
```

## 🚀 Usage
1. Place your `conversations.json` file in the root directory.
2. Run the automation:
```bash
python send_to_perplexity.py
```

## ⚙️ What It Does
- Parses your ChatGPT history
- Summarizes long chats
- Uses Selenium to send them into Perplexity (one by one)
