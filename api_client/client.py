# api_client/client.py

import requests

def fetch_api_data(api_url):
    """
    Fetches and displays data from a given public API URL.

    Args:
        api_url (str): The URL of the API endpoint.
    """
    print(f"Fetching data from API: {api_url}")
    
    try:
        # Send a GET request to the API endpoint
        response = requests.get(api_url, timeout=10)
        
        # Check if the request was successful (status code 200)
        response.raise_for_status()
        
    except requests.exceptions.RequestException as e:
        print(f"Error: API request failed. {e}")
        return

    print("Data fetched successfully. Processing JSON response...")
    
    # Parse the JSON response into a Python list of dictionaries
    todos_data = response.json()
    
    if not todos_data:
        print("API returned no data.")
        return
        
    print("\n--- TODO List from API (First 10 items) ---")
    
    # Loop through the first 10 items and print formatted details
    for todo in todos_data[:10]:
        user_id = todo.get('userId', 'N/A')
        title = todo.get('title', 'No Title')
        completed = todo.get('completed', False)
        
        # Display a checkmark or a cross based on the completion status
        status_icon = "✅" if completed else "❌"
        
        print(f"[{status_icon}] User {user_id}: {title}")

    print("\n-------------------------------------------")


# --- Main Execution ---
if __name__ == "__main__":
    # The endpoint for fetching a list of 'todos' from the JSONPlaceholder API
    JSONPLACEHOLDER_API_URL = 'https://jsonplaceholder.typicode.com/todos'
    fetch_api_data(JSONPLACEHOLDER_API_URL)
