# Project 5: Data Cleaner and Processor

This project is a Python script that demonstrates how to clean and process data from a messy CSV file using the `pandas` library. It takes a raw sales data file, performs several cleaning operations, calculates a new `Total_Price` column, and saves the clean data to a new file.

This type of task is extremely common in data automation and freelance work.

## Features
- Reads data from a CSV file into a pandas DataFrame.
- Removes duplicate rows.
- Handles missing values by filling them with sensible defaults.
- Cleans and converts data types (e.g., removes currency symbols and converts strings to numbers).
- Creates a new column based on calculations from existing data.
- Saves the cleaned, processed data to a new CSV file.

## Libraries Used
- `pandas`: The essential library for data manipulation and analysis in Python.

## Setup & How to Run

1.  **Install Libraries:** Make sure you have Python installed. Then, install `pandas`:
    ```bash
    pip install pandas
    ```

2.  **Check Your Files:** Ensure the `sales_data.csv` file is in the same directory as the `processor.py` script.

3.  **Run the Script:**
    ```
    python processor.py
    ```

After the script runs, a new file named `cleaned_sales_data.csv` will be created in the directory. Open it to see the cleaned and processed data.