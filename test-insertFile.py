import os
import requests

# API endpoint for uploading a file to a specific folder
UPLOAD_ENDPOINT = 'http://localhost:3000/api/insertFile'  # Base URL, the folder name will be appended

# Path of the file you want to upload
FILE_PATH = 'example_results.json'  # Change this to the file you want to upload

# Full folder name where the file should be uploaded
FOLDER_NAME = 'user-452-submission-743'  # You can modify this to any folder name

def main():
    # Ensure the file exists
    if not os.path.exists(FILE_PATH):
        print(f"File not found: {FILE_PATH}")
        return

    # Construct the upload URL
    upload_url = f'{UPLOAD_ENDPOINT}/{FOLDER_NAME}'

    try:
        # Open the file and prepare it for upload
        with open(FILE_PATH, 'rb') as file:
            files = {'file': (os.path.basename(FILE_PATH), file)}

            # Send POST request to upload the file to the specific folder
            response = requests.post(upload_url, files=files)

            # Check if the request was successful
            if response.status_code == 201:
                print(f"File uploaded successfully to folder {FOLDER_NAME}")
            else:
                print(f"Failed to upload file. Status code: {response.status_code}")
                print(response.json())

    except requests.exceptions.RequestException as e:
        print(f"Error uploading file: {e}")

if __name__ == "__main__":
    main()
