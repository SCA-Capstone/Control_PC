import requests

# URL of the uploadFile API
url = "http://localhost:3000/api/uploadFile"  # Change this to the correct endpoint

# Path to the file you want to upload
file_path = "path/to/your/file.txt"

# Prepare the files dictionary to send in the request
files = {
    'file': open(file_path, 'rb')  # Open the file in binary mode
}

# Make the POST request to upload the file
try:
    response = requests.post(url, files=files)

    # Check if the upload was successful
    if response.status_code == 200:
        print("File uploaded successfully.")
        print(response.json())
    else:
        print(f"Error uploading file: {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
