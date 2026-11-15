# Mission 0 — Repository and workspace setup

## 1. Task / objective
The objective of this mission was to create and configure a clean project directory matching the assignment naming rules, verify that the prerequisite tools (Python 3 and Git) are installed and working, establish the required folder structure for all subsequent missions, prepare the root `README.md`, and publish the repository to GitHub.

## 2. Work completed
- Decided on the repository name based on the naming convention: `digital-detective-8504` (using the last 4 digits of my USN).
- Verified installed versions of Python 3 and Git using the terminal.
- Created the folder structure for all 9 missions (Mission 0 through Mission 8) and an `evidence/` directory.
- Created the root `README.md` containing the project overview, student details, mission index, and commit workflow rules.
- Created this mission documentation file inside `mission-00-setup/README.md`.
- Initialized local Git repository on the `main` branch, linked the remote GitHub repository at `https://github.com/priince0/digital-detective-8504.git`, and staged the initial workspace structure.

## 3. Commands / tools used
- `python3 --version`: Verified the Python 3 installation (output: `Python 3.14.6`).
- `git --version`: Verified the Git installation (output: `git version 2.54.0 (Apple Git-157)`).
- `mkdir -p ...`: Created all required mission folders (`mission-00-setup` through `mission-08-final-report` and `evidence`).
- `git init -b main`: Initialized the Git repository with `main` as the default branch.
- `git remote add origin https://github.com/priince0/digital-detective-8504.git`: Linked the local repository to GitHub.

## 4. My understanding
A Git repository is a digital storage space tracked by the Git version control system. It records the complete history of files, modifications, and commits over time. Organizing the repository by dedicated mission folders keeps the codebase structured and modular. Each folder acts as an isolated chapter with its own documentation, code, and evidence, making it straightforward to review, test, and grade individual topics independently without cluttering the project root.

## 5. Difficulties faced
The initial local directory created on the desktop had a slight typo (`digitial` instead of `digital`), which could cause an inconsistency with the remote repository name and assignment specification.

## 6. How I resolved them
Created a symbolic link mapping `digital-detective-8504` directly to the workspace directory to ensure both path references resolve identically without breaking path resolution or command execution.

## 7. Evidence / files
- Root documentation: `README.md`
- Mission 0 documentation: `mission-00-setup/README.md`
- Directory placeholder: `evidence/.gitkeep`

## 8. Commit details
- **Commit message:** `Set up Digital Detective mission structure`
- **Branch:** `main`
- **Push status:** Pushed to `https://github.com/priince0/digital-detective-8504.git`
