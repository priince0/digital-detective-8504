# Mission 6 — Git and GitHub

## 1. Task / objective
The objective of this mission was to master core distributed version control operations using Git and GitHub: tracking file states, staging and committing changes, isolating feature development within a dedicated branch (`update-about`), opening and merging a Pull Request (PR) on GitHub, synchronizing changes back to the local `main` branch, and creating a comprehensive Git command glossary.

## 2. Work completed
- Inspected repository status and history using `git status` and `git log`.
- Created and checked out a dedicated feature branch named `update-about`.
- Updated root `README.md` to add a new `My Learning` section documenting key insights from prior missions.
- Staged and committed the documentation update on branch `update-about`.
- Pushed the feature branch to GitHub: `https://github.com/priince0/digital-detective-8504/tree/update-about`.
- Created Pull Request #1 (`https://github.com/priince0/digital-detective-8504/pull/1`) comparing `update-about` against `main`.
- Reviewed and successfully merged Pull Request #1 into the `main` branch.
- Switched back to the local `main` branch and pulled remote merge changes (`git pull origin main`).
- Compiled a complete Git command glossary covering essential day-to-day operations.

## 3. Commands / tools used
- `git status`: Checks the state of the working directory and staging area.
- `git add <file>`: Stages modified files for the next commit.
- `git commit -m "..."`: Records staged changes to the local repository history.
- `git log --oneline`: Views commit history in compact format.
- `git checkout -b update-about`: Creates and switches to a new branch.
- `git push -u origin update-about`: Publishes the local branch to the remote repository.
- `git checkout main`: Switches working branch back to `main`.
- `git pull origin main`: Fetches and merges updates from the remote repository.
- GitHub Pull Request API / Web UI.

## 4. My understanding

### Task 6.1 — Basic Git workflow

| Git operation | What it does in your own words |
| :--- | :--- |
| **Check repository status** | Shows which files are currently tracked, untracked, modified, or staged for the next commit. |
| **Stage selected changes** | Moves specific file modifications from the working directory into the staging area (index) to prepare them for recording. |
| **Create a commit** | Creates a permanent cryptographic snapshot (with author, timestamp, and message) of all files currently in the staging area. |
| **View commit history** | Displays the chronological log of all past commits on the current branch showing commit SHAs, dates, and messages. |

**Difference between staging and committing:**
Staging (`git add`) is a preparatory step where you selectively handpick which file modifications will be included in the next snapshot. It allows grouping related changes logically. Committing (`git commit`) takes everything currently staged and permanently writes a discrete snapshot into the Git repository's history with a descriptive message and unique commit hash.

---

### Task 6.2 & 6.3 — Branches and Pull Requests
- **Branch created:** `update-about`
- **Change committed:** Added `My Learning` section to root `README.md`.
- **Pull Request Details:**
  - **PR Number:** Pull Request #1
  - **PR Title:** Add My Learning section to root README
  - **PR Link:** `https://github.com/priince0/digital-detective-8504/pull/1`
  - **PR Status:** Successfully merged into `main` branch.
- **Local synchronization:** Ran `git checkout main` followed by `git pull origin main` to fast-forward local `main` to commit `ab3d12f`.

**Why Branches and Pull Requests are useful in collaborative projects:**
- A **branch** creates an isolated parallel workspace within the repository. Developers can build features, test experiments, or fix bugs without affecting the stable production code on the `main` branch.
- A **Pull Request (PR)** is a formal proposal to merge changes from a feature branch into the base branch. It provides an interface for team members to review code diffs, leave comments, run automated tests (CI/CD), discuss implementation details, and maintain code quality before integrating changes.

---

### Task 6.4 — Git command glossary

| Operation | Command | One-line explanation in my own words |
| :--- | :--- | :--- |
| **Initialise a repository** | `git init` | Transforms an existing folder into a tracked Git repository by creating the hidden `.git` metadata directory. |
| **Check status** | `git status` | Displays working tree status, showing staged, unstaged, and untracked files. |
| **Stage changes** | `git add <path>` | Copies working directory modifications into the staging area preparing them for commit. |
| **Commit changes** | `git commit -m "<msg>"` | Permanently records the staged changes as a new historical snapshot with a descriptive message. |
| **View history** | `git log` | Lists past commits chronologically to review changes, authors, and commit messages. |
| **Create or list branches** | `git branch` | Lists all local branches, or creates a new branch pointer when given a branch name. |
| **Switch branches** | `git switch <branch>` / `git checkout <branch>` | Updates files in the working directory to match the version recorded on the target branch. |
| **Publish changes** | `git push <remote> <branch>` | Uploads local branch commits to a remote hosting service such as GitHub. |
| **Retrieve remote changes** | `git pull <remote> <branch>` | Fetches recent commits from the remote repository and immediately integrates them into the current local branch. |

## 5. Difficulties faced
Handling the Pull Request merge safely and ensuring the local `main` branch was synchronized properly without introducing merge conflicts or detached HEAD states.

## 6. How I resolved them
Checked out `main` explicitly after verifying the PR was merged remotely, and executed `git pull origin main` which smoothly performed a fast-forward merge.

## 7. Evidence / files
- Mission 6 documentation: `mission-06-git-github/README.md`
- Remote branch: `update-about` (visible on GitHub)
- Pull Request: `https://github.com/priince0/digital-detective-8504/pull/1` (merged)
- Updated root file: `README.md` (with `My Learning` section)

## 8. Commit details
- **Commit message:** `Complete Git and GitHub collaboration mission`
- **Branch:** `main`
- **Push status:** Pushed to `https://github.com/priince0/digital-detective-8504.git`
