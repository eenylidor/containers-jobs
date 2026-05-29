# Git Workflow Guide: From Scratch to GitHub

This guide documents the exact commands used in this session to initialize, manage, and wipe a repository. 

## 1. Initializing a New Repository
Use these steps when you have a script or file on your computer and want to start a brand-new GitHub project.

```bash
# 1. Create a directory for your project
mkdir -p ~/my-new-project

# 2. Move into that directory
cd ~/my-new-project

# 3. Initialize the folder as a Git repository
git init

# 4. Add your files (e.g., your python script) to the staging area
git add my_script.py

# 5. Create your first 'snapshot' (commit) with a descriptive message
git commit -m "Initial commit: Added my_script.py"

# 6. Rename the default branch to 'main' (modern standard)
git branch -m main
```

## 2. Linking and Uploading to GitHub
Since we are in a container/new environment, you must tell Git where your GitHub repository lives and provide authentication.

```bash
# 1. Add the remote origin URL
# REPLACE <TOKEN> with your actual GitHub Personal Access Token (PAT)
# REPLACE <USER> with your GitHub username
git remote add origin https://<USER>:<TOKEN>@github.com/<USER>/my-new-project.git

# 2. Push your code to the 'main' branch on GitHub
# The '-u' flag links your local 'main' to the remote 'origin/main' for future ease
git push -u origin main
```

## 3. Adding New Files Later
Once the repo is set up, adding more files (like guides or new scripts) is much simpler.

```bash
# 1. Add the specific file
git add GUIDE.md

# 2. Commit the change
git commit -m "Add documentation"

# 3. Push it to GitHub
git push
```

## 4. Wiping a Repository (Deleting all files)
Use this only if you want to clear out all code from the repository while keeping the repo name alive on GitHub.

```bash
# 1. Remove all files in the current directory from Git tracking
git rm -r .

# 2. Commit the deletion
git commit -m "Wipe all content from repository"

# 3. Push the 'empty' state to GitHub
git push origin main
```
