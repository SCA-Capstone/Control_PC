import requests

# URL of the deleteRecord API
url = "http://localhost:3000/api/deleteRecord"  # Change this to your correct API endpoint

# Data containing the ID of the record to delete
data = {
    'id': 1  # Replace this with the actual record ID or identifier
}

# Make the DELETE request to delete the record
try:
    response = requests.delete(url, json=data)

    # Check if the delete operation was successful
    if response.status_code == 200:
        print("Record deleted successfully.")
        print(response.json())  # Print the response from the server
    else:
        print(f"Error deleting record: {response.status_code}")
        print(response.text)  # Print the error response

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
