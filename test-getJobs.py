import requests

# Define the URL of the Next.js API route
url = "http://localhost:3000/api/getJobs"  # Update this URL based on your local or production environment

# Send the GET request to the API route
try:
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        print("Records retrieved successfully:")
        print(data)
    else:
        print(f"Error retrieving records: {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
