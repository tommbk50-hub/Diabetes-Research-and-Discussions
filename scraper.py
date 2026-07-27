import os
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# 1. Discord Setup via Environment Variables
DISCORD_WEBHOOK_URL = os.environ.get('DISCORD_WEBHOOK_URL')

# 2. Set up Chrome options
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

# 3. Initialize the WebDriver
try:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
except Exception as e:
    print(f"Initialization failed: {e}")
    raise

# 4. Search Execution
keywords = ["Type 1 Diabetes", "VX-880", "Tegoprubart"]
all_new_trials = []

for keyword in keywords:
    url = f"https://bepartofresearch.nihr.ac.uk/results/search-results?query={keyword}&location="
    print(f"Fetching data for: {keyword}...")
    driver.get(url)
    
    trials_data = []
    
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='/trial-details/']"))
        )
        time.sleep(2)
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        links = soup.select("a[href*='/trial-details/']")
        
        for link in links:
            href = link.get('href', '')
            study_url = f"https://bepartofresearch.nihr.ac.uk{href}" if href.startswith('/') else href
            
            title = link.get_text(" ", strip=True)
            title = title.replace("Read Study Details for", "").replace("(Opens new tab)", "").strip()
            
            if title and not any(d['Link'] == study_url for d in trials_data):
                if len(title) > 5:
                    trials_data.append({"Keyword": keyword, "Study Title": title, "Link": study_url})
                    all_new_trials.append({"Keyword": keyword, "Study Title": title, "Link": study_url})
                    
    except Exception as e:
        print(f"No active trials found for '{keyword}', or the timeout was reached.")

driver.quit()

# 5. Alert Logic
if all_new_trials:
    print(f"Success! Found {len(all_new_trials)} trials across all terms. Sending Discord alert...")
    
    # Format the message for Discord Markdown
    msg = "🚨 **Clinical Trial Alert**\n\n"
    for trial in all_new_trials:
        msg += f"• **{trial['Keyword']}**: {trial['Study Title']}\n<{trial['Link']}>\n\n"
    
    try:
        # Send HTTP POST request to Discord Webhook
        response = requests.post(DISCORD_WEBHOOK_URL, json={"content": msg})
        
        if response.status_code == 204:
            print("Alert sent successfully!")
        else:
            print(f"Failed to send alert. Status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send Discord message: {e}")
else:
    print("No trials found for any keywords. No alert sent.")
