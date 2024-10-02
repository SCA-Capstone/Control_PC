import requests

# URL of the downloadFile API
url = "http://localhost:3000/api/downloadFile"  # Change this to the correct endpoint

# Name of the file to be downloaded
params = {'filename': 'file.txt'}  # You may need to update 'filename' based on your API logic

# Make the GET request to download the file
try:
    response = requests.get(url, params=params)

    # Check if the download was successful
    if response.status_code == 200:
        # Save the file locally
        with open("downloaded_file.txt", 'wb') as f:
            f.write(response.content)
        print("File downloaded successfully.")
    else:
        print(f"Error downloading file: {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
