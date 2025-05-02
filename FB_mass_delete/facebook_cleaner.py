from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

EMAIL = input("Enter your Facebook email: ")
PASSWORD = input("Enter your Facebook password: ")
USERNAME = input("Enter your Facebook username (from facebook.com/your.username): ")
DATE_THRESHOLD = input("Delete posts/comments from which date? (YYYY-MM-DD or leave empty for all): ")
ENABLE_LOGGING = input("Enable logging? (yes/no): ").lower() == "yes"

if DATE_THRESHOLD:
    try:
        DATE_THRESHOLD = datetime.strptime(DATE_THRESHOLD, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        exit(1)

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")  # Uncomment for headless mode

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

def log(message):
    if ENABLE_LOGGING:
        print(message)

def login():
    driver.get("https://www.facebook.com/")
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys(EMAIL)
    driver.find_element(By.ID, "pass").send_keys(PASSWORD)
    driver.find_element(By.NAME, "login").click()
    time.sleep(5)
    log("Logged in successfully.")

def go_to_activity_log():
    driver.get(f"https://www.facebook.com/{USERNAME}/allactivity")
    time.sleep(5)
    log("Navigated to Activity Log.")

def is_after_threshold(text):
    if not DATE_THRESHOLD:
        return True
    try:
        # Parse visible date string (e.g. "April 2021", "20 Jan 2020")
        return_date = None
        for fmt in ("%d %b %Y", "%B %Y", "%b %Y"):
            try:
                return_date = datetime.strptime(text.strip(), fmt)
                break
            except:
                continue
        if return_date:
            return return_date >= DATE_THRESHOLD
    except:
        return True
    return True

def scroll_and_clean():
    last_height = driver.execute_script("return document.body.scrollHeight")
    scrolls = 0

    while scrolls < 50:
        time.sleep(3)

        actions = driver.find_elements(By.XPATH, "//div[@aria-label='Actions for this post' or                                                     @aria-label='Actions for this comment' or                                                     @aria-label='Ενέργειες για αυτήν την ανάρτηση' or                                                     @aria-label='Ενέργειες για αυτό το σχόλιο']")
        for action in actions:
            try:
                driver.execute_script("arguments[0].scrollIntoView(true);", action)

                parent = action.find_element(By.XPATH, "./ancestor::div[contains(@data-visualcompletion, 'ignore-dynamic')]")
                date_elems = parent.find_elements(By.XPATH, ".//span[contains(@class,'timestamp')]")
                if date_elems and not is_after_threshold(date_elems[0].text):
                    continue

                action.click()
                time.sleep(1)

                delete = None
                try:
                    delete = driver.find_element(By.XPATH, "//span[contains(text(), 'Move to Recycle Bin') or                                                             contains(text(), 'Delete') or                                                             contains(text(), 'Μετακίνηση στον Κάδο') or                                                             contains(text(), 'Διαγραφή')]")
                except:
                    continue

                if delete:
                    delete.click()
                    time.sleep(1)
                    confirm = driver.find_element(By.XPATH, "//div[@aria-label='Move' or                                                               @aria-label='Delete' or                                                               @aria-label='Μετακίνηση' or                                                               @aria-label='Διαγραφή']")
                    confirm.click()
                    log("Deleted an item.")
                    time.sleep(2)
            except Exception as e:
                log(f"Error: {e}")
                continue

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        scrolls += 1

try:
    login()
    go_to_activity_log()
    scroll_and_clean()
finally:
    driver.quit()
    log("Script completed.")
