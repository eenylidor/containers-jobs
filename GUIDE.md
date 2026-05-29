# Setup Guide: containers-jobs

This guide explains how to restore this repository and continue working when starting from a fresh or new container environment.

## 1. Restore the Repository
When you are in a new terminal session or a brand-new container, run the following command to download your code:

```bash
git clone https://github.com/eenylor/containers-jobs.git
```

Then, move into the project directory:

```bash
cd containers-jobs
```

## 2. Adding New Scripts
To add a new script (e.g., `myscript.py`) to this repository, follow these standard Git steps:

1. **Place your file** inside the `containers-jobs` folder.
2. **Stage the file**:
   ```bash
   git add myscript.py
   ```
3. **Commit the change**:
   ```bash
   git commit -m "Added myscript.py"
   ```
4. **Push to GitHub**:
   ```bash
   git push origin main
   ```

## 3. Authentication Note
If `git push` asks for a username and password:
- **Username**: Your GitHub username (e.g., `eenylidor`)
- **Password**: Use your **GitHub Personal Access Token (PAT)**, NOT your GitHub account password.

## 4. Deleting the Repository
If you no longer need this repository, you can delete it via the GitHub web interface by going to:
`Settings` -> `Danger Zone` -> `Delete this repository`.
