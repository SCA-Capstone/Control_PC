# NextAPIClient Automation

`NextAPIClient` is a Python script designed to interact with a Next.js API, managing job records, file uploads, and task status updates. It enables API-based job submission, filtering, and handling for specific job configurations (`python`, `cpp`, `java`). Each job can include a configuration-specific task, file handling, and status management, making it versatile for various automation tasks.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Usage](#usage)
   - [Configuration](#configuration)
   - [API Methods](#api-methods)
   - [Example Workflow](#example-workflow)
4. [Customization](#customization)

## Prerequisites

- Python 3.6 or higher
- Required libraries: `requests`, `json`, `os`, `time`, `dotenv`
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
   BASE_URL=<Your Next.js API URL>
   API_AUTH_TOKEN=<Your API Key>
   ```

## Usage

### Configuration

The main configurations the script handles include `python`, `cpp`, and `java` jobs. These configurations dictate specific handling and file processing methods within the workflow.

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

    while True:
        data = client.get_python_jobs()
        ids = [job['id'] for job in data] if data else []

        for job_id in ids:
            print(f"Processing job with ID: {job_id}")
            folder = client.get_folder(folder_id=job_id)
            client.update_task_status(job_id)

            # Add configuration-specific tasks
            ##################################

            # Upload results
            client.insert_file(folder_name=folder, file_path='example_results.json')
            client.update_task_status(job_id)

        # Pause between API calls
        time.sleep(20)
```

### Customization

Add configuration-specific tasks for `cpp` and `java` jobs within the loop by modifying the `# Add configuration-specific tasks` section.
