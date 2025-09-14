# web_scraper/scraper.py

import requests
from bs4 import BeautifulSoup # type: ignore
import csv

def scrape_books(url):
    """
    Scrapes book titles and prices from the given URL and saves them to a CSV file.

    Args:
        url (str): The URL of the books.toscrape.com page to scrape.
        
    Returns:
        None. Prints status messages and writes data to 'books.csv'.
    """
    print(f"Attempting to fetch content from: {url}")
    
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url, timeout=10)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: Could not fetch the webpage. {e}")
        return

    print("Webpage fetched successfully! Parsing HTML...")
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all article elements with the class 'product_pod'
    # Each of these articles represents a single book
    books = soup.find_all('article', class_='product_pod')
    
    if not books:
        print("No books found on the page. The website structure might have changed.")
        return
        
    scraped_data = []
    
    # Loop through each book found
    for book in books:
        # Extract the title from the <h3> tag's <a> element's 'title' attribute
        title_element = book.find('h3').find('a')
        title = title_element['title'] if title_element else 'No Title Found'
        
        # Extract the price from the <p> element with the class 'price_color'
        price_element = book.find('p', class_='price_color')
        price = price_element.get_text() if price_element else 'No Price Found'
        
        scraped_data.append({'title': title, 'price': price})

    # Save the data to a CSV file
    try:
        with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(scraped_data)
        print(f"\nSuccessfully scraped {len(scraped_data)} books and saved to books.csv")
    except IOError as e:
        print(f"Error writing to CSV file. {e}")


# --- Main Execution ---
if __name__ == "__main__":
    # The URL of the website we want to scrape
    TARGET_URL = 'http://books.toscrape.com/'
    scrape_books(TARGET_URL)
