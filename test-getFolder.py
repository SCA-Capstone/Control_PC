import os
import requests

# API endpoint for fetching files based on folder ID (last three digits)
api_endpoint = 'http://localhost:3000/api/getFile/743'  # Change this to your actual endpoint

# Directory to save downloaded files
download_dir = 'test'

# Ensure the directory exists
os.makedirs(download_dir, exist_ok=True)

def download_files():
    try:
        # Send GET request to API
        response = requests.get(api_endpoint)
        print(response)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the response JSON
        data = response.json()
        files = data.get('files', [])

        if not files:
            print("No files found for the given folder ID.")
            return

        # Download each file
        for file_info in files:
            file_name = file_info['fileName']
            file_url = file_info['publicUrl']

            # Download the file content
            file_response = requests.get(file_url)
            file_response.raise_for_status()  # Check for errors

            # Save the file into the test directory
            file_path = os.path.join(download_dir, file_name)
            with open(file_path, 'wb') as file:
                file.write(file_response.content)

            print(f"Downloaded: {file_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching files: {e}")

if __name__ == "__main__":
    download_files()
