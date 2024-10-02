import requests
import json

# Define the URL of your Next.js API route
url = "http://localhost:3000/api/insertRecord"  # Change this to the correct URL of your running Next.js app

# Create the data payload (the record you want to insert)
data = {
    "name": "John Doe",
    "email": "john@example.com",
    "company": "JohnDoeInc",
    "userId": "1234"
}

# Send the POST request to the Next.js API route
try:
    response = requests.post(
        url, 
        headers={'Content-Type': 'application/json'}, 
        data=json.dumps(data)
    )

    # Check if the request was successful
    if response.status_code == 200:
        print("Record inserted successfully")
        print("Response:", response.json())
    else:
        print(f"Error inserting record: {response.status_code}")
        print("Response:", response.json())

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
