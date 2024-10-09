import requests
import json

url = 'http://localhost:3000/api/insertRecord'  # Change to your actual API URL

payload = {
    "id": 678,
    "created_at": "2024-09-19T02:24:58.608Z",
    "name": "testing insert",
    "email": "example@gmail.com",
    "company": "Crumble",
    "files": True,
    "userId": 500,
    "status": "waiting"
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

if response.status_code == 200:
    print('Success:', response.json())
else:
    print('Error:', response.status_code, response.text)
