# NextAPIClient Automation

`NextAPIClient` is a Python script designed to interact with a Next.js API, managing job records, file uploads, and task status updates. It enables API-based job submission, filtering, and handling for specific job configurations (`python`, `cpp`, `java`). Each job can include a configuration-specific task, file handling, and status management, making it versatile for various automation tasks.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Usage](#usage)
   - [Configuration](#configuration)
   - [API Methods](#api-methods)
   - [Example Workflow](#example-workflow)

## Prerequisites

- Python 3.6 or higher
- Required libraries: `requests`, `json`, `os`, `time`, `dotenv`, `subprocess`
- Next.js API endpoint and API key, stored in a `.env` file

## Installation

1. **Clone the Repository**
   ```bash
   git clone 
   cd 
   ```

2. **Install Dependencies**
   ```bash
   pip install requests python-dotenv
   ```

3. **Set Up Environment Variables**

   Create a `.env` file in the project directory with the following content:
   ```bash
   BASE_URL=<Next.js API URL>
   API_AUTH_TOKEN=<API Key>
   ```

## Usage

### Configuration

The main configurations the script handles include `python`, `cpp`, and `java` jobs. These configurations dictate specific handling and file processing methods within the workflow.

Each `bot` will grab its specific job files and throw it in assossiated `config_files` directory to be accessed anf compiled. Standard out and Standard error will be recorded and thrown in `config_output` to be uploaded. For example, the python bot will download necessary files into `python_files` and put the output from the test into `python_output`. Additional work will be needed to manage directory space because as of now all files are being overwritten instead of deleted after use.

### API Methods

1. **`insert_record`**: Adds a job record to the database.
2. **`get_jobs`**: Retrieves all job records.
3. **`get_submitted_jobs`**: Filters jobs with the status `submitted`.
4. **`get_config_jobs`**: Filters jobs with the status `submitted` and configuration `Python/C++/Java`.
5. **`insert_file`**: Uploads a file to a designated folder.
6. **`get_folder`**: Downloads all files from a specified folder ID.
7. **`update_task_status`**: Updates the status of a specific job to manage its progress.

### Example Workflow

The script performs a recurring loop to automate job processing by:
1. Fetching jobs with the `submitted` status and specific configurations.
2. Iterating over the job IDs to:
   - Download associated files for each job.
   - Perform configuration-specific tasks (e.g., running a script or analysis).
   - Upload results.
   - Update job status from `in progress` to `complete`.

Example usage code is in the main loop:

```python
if __name__ == "__main__":
    client = NextAPIClient()

    # Create output directory if it doesn't exist
    output_dir = 'python_output'
    os.makedirs(output_dir, exist_ok=True)

    while True:

        # Limit infinite loop hitting api too quick
        time.sleep(1)

        # Get jobs
        data = client.get_python_jobs()
        print(data)

        if data == None:
            time.sleep(60)
            continue

        # Extract 'id' values
        ids = [job['id'] for job in data]
        print(ids)

        # Iterate over each id in ids and perform actions
        for job_id in ids:
            print(f"Processing job with ID: {job_id}")

            # Get files from a folder
            folder = client.get_folder(folder_id=job_id)
            # print(folder)

            # Job should be 'in progress' now
            client.update_task_status(job_id)

            # Add Config Specific Tasks Here
            ################################
            # Run a shell command and capture both stdout and stderr
            stdout_path = os.path.join(output_dir, f"stdout.txt")
            stderr_path = os.path.join(output_dir, f"stderr.txt")

            with open(stdout_path, 'w') as stdout_file, open(stderr_path, 'w') as stderr_file:
                result = subprocess.run(
                #change here for different commands
                ["python", "python_files/test.py"],
                stdout=stdout_file,
                stderr=stderr_file,
                text=True
            )

            # Loop through the output directory and insert each file into the folder
            for output_file in os.listdir(output_dir):
                file_path = os.path.join(output_dir, output_file)
                if os.path.isfile(file_path):
                    # Insert each file in the output directory
                    client.insert_file(folder_name=folder, file_path=file_path)
           
            # Job should be 'complete' now
            client.update_task_status(job_id)
            

        # Limit infinite loop hitting api too quick
        time.sleep(20)
```

