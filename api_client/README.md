# Project 4: Simple API Client

This project is a basic API client that demonstrates how to interact with a public REST API. It sends a `GET` request to the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/), a free online API for testing and prototyping. The script fetches a list of 'todos' and prints selected information for the first few items.

## Features
- Makes an HTTP `GET` request to a public API endpoint.
- Handles the `JSON` response.
- Parses the `JSON` data to extract useful information.
- Displays the formatted data in the console.

## Libraries Used
- `requests`: The standard library for making HTTP requests in Python.

## Setup & How to Run

**Install Libraries:**
If you don't have it already, install the `requests` library:

    pip install requests 

**Run the Script:**
Navigate to this directory in your terminal and run the script:

    python client.py

The script will fetch a list of todos from the API and print the User ID, title, and completion status for the first 10 items in the list.
