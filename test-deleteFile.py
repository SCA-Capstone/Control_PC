import requests

# URL of the deleteFile API
url = "http://localhost:3000/api/deleteFile"  # Change this to the correct endpoint

# Data containing the filename to delete
data = {
    'filename': 'file.txt'  # Adjust this to match the file you want to delete
}

# Make the DELETE request to delete the file
try:
    response = requests.delete(url, json=data)

    # Check if the delete operation was successful
    if response.status_code == 200:
        print("File deleted successfully.")
        print(response.json())
    else:
        print(f"Error deleting file: {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
