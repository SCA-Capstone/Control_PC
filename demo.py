import requests
import json
import os
import time


class NextAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def insert_record(self, payload):
        url = f'{self.base_url}/insertRecord'
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.post(
                url, data=json.dumps(payload), headers=headers)
            if response.status_code == 200:
                print('Record inserted successfully:', response.json())
            else:
                print(
                    f'Error inserting record: {response.status_code}', response.text)
        except requests.exceptions.RequestException as e:
            print(f'Request failed: {e}')

    def get_jobs(self):
        url = f'{self.base_url}/getJobs'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print('Records retrieved successfully:', response.json())
            else:
                print(
                    f'Error retrieving records: {response.status_code}', response.text)
        except requests.exceptions.RequestException as e:
            print(f'Request failed: {e}')

    def get_submitted_jobs(self):
        url = f'{self.base_url}/getJobs'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                # Filter jobs where status is 'submitted'
                submitted_jobs = [job for job in data if job.get(
                    'status') == 'submitted']
                if submitted_jobs:
                    print('Submitted jobs retrieved successfully:', submitted_jobs)
                else:
                    print('No submitted jobs found.')
            else:
                print(
                    f'Error retrieving records: {response.status_code}', response.text)
        except requests.exceptions.RequestException as e:
            print(f'Request failed: {e}')

    def insert_file(self, folder_name, file_path):
        upload_url = f'{self.base_url}/insertFile/{folder_name}'

        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return

        try:
            with open(file_path, 'rb') as file:
                files = {'file': (os.path.basename(file_path), file)}
                response = requests.post(upload_url, files=files)

                if response.status_code == 201:
                    print(
                        f"File uploaded successfully to folder {folder_name}")
                else:
                    print(
                        f"Failed to upload file. Status code: {response.status_code}", response.json())
        except requests.exceptions.RequestException as e:
            print(f"Error uploading file: {e}")

    def get_folder(self, folder_id, download_dir='test'):
        # API endpoint to fetch folders and their files
        url = f'{self.base_url}/getFolder/{folder_id}'

        os.makedirs(download_dir, exist_ok=True)

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad status codes

            data = response.json()
            files = data.get('files', [])
            folder_name = data.get('folderName', '')  # Assuming API returns folder name

            if not files:
                print(f"No files found for folder ID {folder_id}.")
                return

            print(f"Folder found: {folder_name}")

            # Download each file
            for file_info in files:
                file_name = file_info['fileName']
                file_url = file_info['publicUrl']

                file_response = requests.get(file_url)
                file_response.raise_for_status()

                file_path = os.path.join(download_dir, file_name)
                with open(file_path, 'wb') as file:
                    file.write(file_response.content)

                print(f"Downloaded: {file_name}")

            return folder_name  # Return the full folder name
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching files: {e}")


    def update_task_status(self, id):
        # API endpoint for updating the task status
        url = f'{self.base_url}/updateStatus/{id}'

        try:
            # Send POST request to the Next.js API with the task ID
            response = requests.post(url)

            # Check if the request was successful
            if response.status_code == 200:
                data = response.json()
                print(f"Status updated successfully: {data['newStatus']}")
            else:
                print(
                    f"Failed to update status. Status code: {response.status_code}")
                print(response.json())
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")


# Example usage:
if __name__ == "__main__":
    client = NextAPIClient(base_url='http://localhost:3000/api')

    # Get jobs
    client.get_submitted_jobs()

    # Get files from a folder
    folder = client.get_folder(folder_id='743')
    client.update_task_status('743')
    #print(folder)

    time.sleep(30)

    client.insert_file(folder_name=folder, file_path='example_results.json')
    client.update_task_status('743')