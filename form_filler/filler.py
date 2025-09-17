# form_filler/filler.py

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def fill_form(csv_path):
    """
    Reads data from a CSV and fills out a sample web form for each row.
    
    Args:
        csv_path (str): The path to the input CSV file.
    """
    # --- 1. Setup ---
    if not os.path.exists(csv_path):
        print(f"Error: The file '{csv_path}' was not found.")
        return

    try:
        # Use pandas to read data from the CSV file
        df = pd.read_csv(csv_path)
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return

    # Path to your chromedriver executable
    # Assumes chromedriver is in the same directory as the script
    webdriver_path = './chromedriver'
    service = Service(executable_path=webdriver_path)
    
    # Initialize the Chrome browser driver
    try:
        driver = webdriver.Chrome(service=service)
    except Exception as e:
        print(f"Error initializing WebDriver. Make sure chromedriver is in the path. {e}")
        return

    # The URL of the sample form
    form_url = 'https://www.selenium.dev/selenium/web/web-form.html'
    
    print(f"Successfully read {len(df)} rows from {csv_path}. Starting browser automation.")

    # --- 2. Automation Loop ---
    for index, row in df.iterrows():
        try:
            print(f"\nProcessing entry #{index + 1}: {row['first_name']} {row['last_name']}")
            
            # Navigate to the form page
            driver.get(form_url)
            
            # Use WebDriverWait to ensure the page and elements are loaded
            wait = WebDriverWait(driver, 10)
            
            # Find form elements by their name attribute and fill them
            wait.until(EC.presence_of_element_located((By.NAME, 'my-text'))).send_keys(f"{row['first_name']} {row['last_name']}")
            wait.until(EC.presence_of_element_located((By.NAME, 'my-password'))).send_keys("password123") # Dummy password
            wait.until(EC.presence_of_element_located((By.NAME, 'my-textarea'))).send_keys(row['message'])
            
            # Find and click the submit button
            submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
            submit_button.click()
            
            # Wait for the success message to appear to confirm submission
            success_message = wait.until(EC.presence_of_element_located((By.ID, 'message')))
            print(f"Success! Response: {success_message.text}")
            
            # Wait for a moment to observe the result before the next iteration
            time.sleep(2)

        except Exception as e:
            print(f"An error occurred while processing row {index + 1}: {e}")
            continue

    # --- 3. Teardown ---
    print("\nAutomation complete. Closing the browser.")
    driver.quit()


# --- Main Execution ---
if __name__ == "__main__":
    CSV_FILE_PATH = 'data.csv'
    fill_form(CSV_FILE_PATH)
