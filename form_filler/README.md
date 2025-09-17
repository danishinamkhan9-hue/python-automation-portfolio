# Project 3: Automated Form Filler Bot

This project demonstrates how to automate data entry using Python. The script reads contact information from a `data.csv` file and automatically fills it into a sample web form using `Selenium`.

## Features
- Reads structured data from a CSV file using `Pandas`.
- Launches a web browser (Chrome) and navigates to a specific URL.
- Locates form fields on the webpage.
- Enters the data from the CSV into the form, row by row.
- Submits the form for each entry.

## Libraries Used
- `selenium`: For automating web browser interaction.
- `pandas`: For reading and processing data from the CSV file.

## Setup & How to Run

1.  **Install Libraries:**
    ```bash
    pip install selenium pandas
    ```

2.  **Install WebDriver:** This script requires a WebDriver to control the browser. Download the `chromedriver` that matches your version of Google Chrome from [the official Chrome for Testing repository](https://googlechromelabs.github.io/chrome-for-testing/). Place the `chromedriver` executable in the same directory as this script.

3.  **Create `data.csv`:** In the same directory, create a file named `data.csv` with the following content:
    ```csv
    first_name,last_name,email,message
    John,Doe,john.doe@example.com,This is a test message.
    Jane,Smith,jane.smith@example.com,Hello from an automated script!
    Peter,Jones,peter.jones@example.com,Selenium is awesome.
    ```

4.  **Run the Script:**
    ```
    python filler.py
    ```

The script will open a Chrome window, navigate to a form, fill it out with the data from the CSV, submit it, and repeat the process for all rows in the file.