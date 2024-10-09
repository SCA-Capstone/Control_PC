import requests

# URL for the API endpoint
url = 'http://localhost:3000/api/getFile/424'

# Send a GET request to the endpoint
try:
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP errors

    # Parse the JSON response (assuming the link is provided in a JSON format)
    data = response.json()

    # Extract the file link from the response (assuming it returns 'file_url' as key)
    file_url = data.get('publicUrl')

    if not file_url:
        print("File URL not found in the response")
    else:
        # Name of the file to save
        new_file_name = 'downloaded-file'

        # Send a GET request to download the file
        print(f"Downloading file from {file_url}...")
        file_response = requests.get(file_url, stream=True)
        file_response.raise_for_status()  # Check if the download was successful

        # Write the content to a file while downloading
        with open(new_file_name, 'wb') as file:
            for chunk in file_response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"File downloaded and saved as '{new_file_name}'.")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
