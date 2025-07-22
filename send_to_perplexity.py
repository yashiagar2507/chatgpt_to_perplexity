import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

# === CONFIG ===
row_number = 1
excel_file = 'chat_history.xlsx'

# === Clean emoji/unicode outside BMP ===
def strip_non_bmp(text):
    return ''.join(c for c in text if ord(c) <= 0xFFFF)

# === Load selected chat ===
df = pd.read_excel(excel_file)
row = df.iloc[row_number - 1]
title = row["Title"]
conversation = row["Conversation"]
cleaned_convo = strip_non_bmp(conversation)
prompt = f"Here’s a previous ChatGPT conversation titled '{title}'. Please reflect or continue:\n\n{cleaned_convo}"

# === Launch browser ===
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
            input_box.send_keys(prompt)
            time.sleep(1)

            # Submit using JavaScript (simulate real Enter keypress)
            driver.execute_script("""
                const box = document.querySelector("div[contenteditable='true']");
                if (box) {
                    box.dispatchEvent(new InputEvent("input", { bubbles: true }));
                    const event = new KeyboardEvent("keydown", {
                        bubbles: true,
                        cancelable: true,
                        key: "Enter",
                        code: "Enter",
                        keyCode: 13
                    });
                    box.dispatchEvent(event);
                }
            """)
            print(f"✅ Sent chat via JS: {title}")
            break
        except StaleElementReferenceException:
            print(f"⚠️ Attempt {attempt + 1} failed due to stale element. Retrying...")
            time.sleep(2)
    else:
        print("❌ Failed after 3 attempts due to stale element.")

except Exception as e:
    print("❌ Failed to send conversation:", e)

input("Press ENTER to close the browser...")
driver.quit()
