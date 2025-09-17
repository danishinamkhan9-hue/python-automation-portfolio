# data_processor/processor.py

import pandas as pd
import os

def process_sales_data(input_file, output_file):
    """
    Reads a messy sales CSV, cleans the data, calculates total price,
    and saves the result to a new CSV file.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the cleaned CSV file.
    """
    # --- 1. Load Data ---
    if not os.path.exists(input_file):
        print(f"Error: The input file '{input_file}' was not found.")
        return

    print(f"Loading data from '{input_file}'...")
    try:
        # Read the csv file into a pandas DataFrame
        df = pd.read_csv(input_file)
        print("Original Data:")
        print(df)
        print("\n" + "="*30 + "\n")
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return

    # --- 2. Clean Data ---
    print("Starting data cleaning process...")

    # a) Remove duplicate rows
    initial_rows = len(df)
    df.drop_duplicates(inplace=True)
    rows_after_duplicates = len(df)
    print(f"- Removed {initial_rows - rows_after_duplicates} duplicate row(s).")

    # b) Handle missing 'Quantity' values - fill with 1 as a default
    missing_qty_count = df['Quantity'].isnull().sum()
    # Coerce to numeric, making non-numbers NaN, then fill NaN with 1
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce').fillna(1).astype(int)
    print(f"- Handled {missing_qty_count} missing 'Quantity' value(s) by setting them to 1.")

    # c) Handle missing 'Date' values - fill with 'Unknown'
    missing_date_count = df['Date'].isnull().sum()
    df['Date'].fillna('Unknown', inplace=True)
    print(f"- Handled {missing_date_count} missing 'Date' value(s).")
    
    # d) Clean and convert 'Price' column
    # Remove '$' and convert the column to a numeric (float) type
    df['Price'] = df['Price'].replace({'\$': ''}, regex=True).astype(float)
    print("- Cleaned '$' from 'Price' column and converted it to a number.")

    # --- 3. Process Data ---
    print("\nProcessing data...")
    
    # Create a new 'Total_Price' column
    df['Total_Price'] = df['Quantity'] * df['Price']
    print("- Calculated new 'Total_Price' column.")

    # --- 4. Save Data ---
    try:
        df.to_csv(output_file, index=False)
        print(f"\nSuccessfully saved cleaned data to '{output_file}'.")
        print("\nCleaned Data:")
        print(df)
    except IOError as e:
        print(f"Error saving the file: {e}")


# --- Main Execution ---
if __name__ == "__main__":
    INPUT_CSV = 'sales_data.csv'
    OUTPUT_CSV = 'cleaned_sales_data.csv'
    process_sales_data(INPUT_CSV, OUTPUT_CSV)
