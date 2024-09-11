# How to Set Up Git for the First Time

## Introduction

Setting up Git for the first time involves configuring your user information, setting up SSH keys for secure communication with GitHub, and ensuring your local Git environment is correctly configured to push changes to a remote repository. This guide will walk you through the necessary steps, including managing files and folders in your repository.

## 1. Configure Git User Information

When you set up Git, it is important to configure your user information. This information is used to label the commits you make to the repository.

### Steps:

1. **Open Terminal or Command Prompt:**
   - For Windows, open Command Prompt or Git Bash.
   - For macOS/Linux, open the Terminal.

2. **Set Global Username and Email:**
   Run the following commands to set your global username and email address:

   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

   **Why:** The `--global` flag ensures that these settings apply to all repositories on your machine. Git uses this information to identify the author of each commit.

## 2. Initialize a New Git Repository

To start using Git in a new project, you need to initialize a Git repository in your project directory.

### Steps:

1. **Navigate to Your Project Directory:**
   ```bash
   cd path/to/your/project
   ```

2. **Initialize Git Repository:**
   ```bash
   git init
   ```

   **Why:** This creates a new `.git` directory in your project, which Git uses to track changes.

## 3. Add Files and Folders to the Repository

Once your repository is initialized, you need to add files and folders to it. In this case, you have a folder of images and a `model.ipynb` file.

### Steps:

1. **Add Files:**
   ```bash
   git add .
   ```

   **Why:** The `git add .` command stages all changes in your working directory for the next commit. This includes the `model.ipynb` file and any other files or folders like your images.

2. **Verify Changes:**
   Run `git status` to check which files are staged for commit.

   ```bash
   git status
   ```

   **Why:** This command shows the status of changes in your working directory and staging area.

## 4. Commit Changes

Committing saves the staged changes to the local repository.

### Steps:

1. **Commit Files:**
   ```bash
   git commit -m "Initial commit with model.ipynb and images folder"
   ```

   **Why:** The commit message should briefly describe the changes made. This helps track the history of your project.

## 5. Set Up Remote Repository

To push your commits to a remote repository like GitHub, you need to add a remote URL.

### Steps:

1. **Add Remote Repository:**
   ```bash
   git remote add origin git@github.com:username/repository.git
   ```

   **Why:** This links your local repository with the remote one on GitHub, allowing you to push and pull changes.

## 6. Set Up SSH Key for Authentication

SSH keys are used for secure communication between your machine and GitHub.

### Steps:

1. **Generate SSH Key:**
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your.email@example.com"
   ```
   Follow the prompts to save the key and optionally add a passphrase.

2. **Add SSH Key to GitHub:**
   - Copy the contents of your public key (typically found at `~/.ssh/id_rsa.pub`).
   - Go to GitHub Settings > SSH and GPG keys > New SSH key, and paste your public key there.

3. **Test SSH Connection:**
   ```bash
   ssh -T git@github.com
   ```

   **Why:** The SSH key allows GitHub to authenticate you without requiring a password every time. Testing the connection ensures that the key was added correctly.

## 7. Push Changes to Remote Repository

With everything set up, you can now push your local changes to the remote repository.

### Steps:

1. **Push Changes:**
   ```bash
   git push -u origin main
   ```

   **Why:** The `-u` flag sets the upstream branch for the local `main` branch, allowing you to use `git push` without specifying the remote branch in the future.

## 8. Troubleshooting Common Issues

- **Permission Denied (publickey):**
  - Ensure your SSH key is correctly added to GitHub.
  - Verify the SSH key is being used by running `ssh-add -l`.

- **`chmod` Not Recognized:**
  - On Windows, use Git Bash or PowerShell to set file permissions if needed.

## Conclusion

By following these steps, you’ve set up Git to manage your project and securely communicate with GitHub. You have also added important files and folders, including a Jupyter notebook and images.
