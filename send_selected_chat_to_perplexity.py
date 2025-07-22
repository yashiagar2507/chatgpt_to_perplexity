import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

# === CONFIG ===
row_number = 24  # Change this to choose a different conversation
excel_file = 'chat_history.xlsx'

# === Helper: Strip unsupported emoji/unicode for ChromeDriver ===
def strip_non_bmp(text):
    return ''.join(c for c in text if ord(c) <= 0xFFFF)

# === Load the selected conversation ===
df = pd.read_excel(excel_file)
row = df.iloc[row_number - 1]
title = row["Title"]
conversation = row["Conversation"]
cleaned_convo = strip_non_bmp(conversation)

# === Final prompt with follow-up chat mode line ===
prompt = (
    f"Here’s a previous ChatGPT conversation titled '{title}'.\n\n"
    f"{cleaned_convo}\n\n"
    "👉 This is the chat I had with ChatGPT, and now give me response for next messages that I’ll send."
)

# === Start browser and open Perplexity ===
driver = webdriver.Chrome()
driver.get("https://www.perplexity.ai")
wait = WebDriverWait(driver, 20)

try:
    input_locator = (By.CSS_SELECTOR, "div[contenteditable='true']")
    wait.until(EC.presence_of_element_located(input_locator))

    for attempt in range(3):
        try:
            input_box = driver.find_element(*input_locator)
            input_box.click()
            time.sleep(0.5)

            # Simulate typing and Enter using ActionChains
            actions = ActionChains(driver)
            actions.move_to_element(input_box)
            actions.click()
            actions.send_keys(prompt)
            actions.send_keys(Keys.ENTER)
            actions.perform()

            print(f"✅ Sent chat: {title}")
            break
        except StaleElementReferenceException:
            print(f"⚠️ Attempt {attempt + 1} failed due to stale element. Retrying...")
            time.sleep(2)
    else:
        print("❌ Failed after 3 attempts due to stale input box.")

except Exception as e:
    print("❌ Failed to send conversation:", e)

# === Leave browser open for manual follow-up ===
print("\n🗨️ Prompt sent. You can now continue chatting manually in Perplexity.")
input("⏸️ Press ENTER to close the browser when you're done...")
driver.quit()
