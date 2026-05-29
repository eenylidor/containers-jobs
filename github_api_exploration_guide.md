# GitHub API Exploration Guide

This guide explains how to programmatically list your GitHub repositories using the GitHub REST API without downloading or cloning them.

## 1. The Concept: Using the REST API
Instead of using `git clone` (which downloads everything), we use **API requests**. We send a lightweight request to a specific URL, and GitHub sends back a small text response containing only the information we asked for (like names, descriptions, or star counts).

## 2. Prerequisites
To interact with your private data, you need a **GitHub Personal Access Token (PAT)**.
*   **Permissions needed:** `repo` (to see private repositories) or `public_repo`.
*   **Security Warning:** Never hardcode your token in a script that you intend to push to a public repository!

## _3. Method A: Using `curl` (The Quick Terminal Way)_
You can check your repositories directly from the command line using `curl`. This is great for quick checks without writing any code.

```bash
# Replace <YOUR_TOKEN> with your actual PAT
curl -H "Authorization: token <YOUR_TOKEN>" \
     https://api.github.com/user/repos
```

## 4. Method B: Using Python (The Automated Way)
If you want to process the list (e.g., filter for specific names, or count them), use a Python script with `urllib` or `requests`.

**Here is the logic I used in our session:**

```python
import urllib.request
import json

# 1. Configuration
TOKEN = 'your_token_here'
URL = 'https://api.github.com/user/repos?per_page=100'
HEADERS = {'Authorization': f'token {TOKEN}'}

def list_repos():
    try:
        # 2. Create the request object
        req = urllib.request.Request(URL, headers=HEADERS)
        
        # 3. Send the request and read the response
        with urllib.request.urlopen(req) as response:
            # Parse the JSON text into a Python list
            repos_data = json.loads(response.read().decode())
            
            # 4. Extract just the names of the repos
            repo_names = [repo['name'] for repo in repos_data]
            
            print("Your Repositories:")
            for name in repo_names:
                print(f"- {name}")
                
    except Exception as e:
        print(f"Error accessing GitHub: {e}")

if __name__ == "__main__":
    list_repos()
```

## 5. Summary of Steps Performed
1.  **Request:** Sent a `GET` request to the `/user/repos` endpoint.
2.  **Authentication:** Passed the PAT in the `Authorization` header.
3.  **Parsing:** Used `json.loads()` to turn the raw text response into a searchable Python list.
4.  **Filtering:** Iterated through the list to print only the `name` field of each repository object.
