# Mission 0 — Repository and workspace setup

## 1. Task / objective
The goal of this first mission was to set up my workspace for the assignment. I needed to pick a proper repository name using the last four digits of my USN, verify that Python 3 and Git are installed on my laptop, set up the folder structure for all nine missions, make a root `README.md`, and push the initial project to GitHub.

## 2. Work completed
- Chose my repository name following the assignment rules: `digital-detective-8504` (using my USN digits 8504).
- Checked my installed versions of Python 3 and Git in Terminal.
- Created all the folders for Mission 0 through Mission 8, along with an `evidence/` folder.
- Wrote the main root `README.md` to introduce the project, list the missions, and provide links.
- Set up Git locally on the `main` branch, linked it to my GitHub repository, and pushed the initial setup.

## 3. Commands / tools used
- `python3 --version`: Checked that Python 3 was installed (got `Python 3.14.6`).
- `git --version`: Checked that Git was installed (got `git version 2.54.0`).
- `mkdir -p ...`: Created the mission folders from `mission-00-setup` to `mission-08-final-report`.
- `git init -b main`: Initialized a new Git repository with `main` as the default branch.
- `git remote add origin https://github.com/priince0/digital-detective-8504.git`: Connected my local folder to my GitHub repo.

## 4. My understanding
A Git repository is essentially a folder tracked by Git so that you can record the history of your files as you work. I organized the assignment into separate mission folders because having a dedicated folder for each topic makes everything clean and easy to find. Each mission has its own README and files, so anyone reviewing the project can look at one specific topic without getting lost.

## 5. Difficulties faced
My initial local folder on the desktop had a small typing mistake in the name (`digitial` with an extra i instead of `digital`), which did not match the GitHub repository name.

## 6. How I resolved them
I made a symbolic link so that both paths refer to the exact same directory, making sure the local folder and the online repository name match up without breaking anything.

## 7. Evidence / files
- Root README: `README.md`
- Mission setup notes: `mission-00-setup/README.md`
- Evidence folder: `evidence/.gitkeep`

## 8. Commit details
- **Commit message:** `Set up Digital Detective mission structure`
- **Branch:** `main`
- **Push status:** Pushed to GitHub
