# Project 1: Simple Web Scraper

This project contains a Python script that scrapes the titles and prices of books from [Books to Scrape](http://books.toscrape.com/), a website designed for web scraping practice.

## Features
- Navigates to a target website.
- Parses HTML content using `BeautifulSoup`.
- Extracts specific data points (book titles and prices).
- Prints the extracted data to the console.

## Libraries Used
- `requests`: For making HTTP requests to get the website's HTML.
- `beautifulsoup4`: For parsing the HTML and extracting data.

## Setup & How to Run

**Install Libraries:**
Make sure you have Python installed. Then, install the required libraries using pip:

    pip install requests beautifulsoup4

**Run the Script:**
Navigate to this directory in your terminal and run the script:

    python scraper.py


The script will print a list of book titles and their corresponding prices found on the first page of the website.