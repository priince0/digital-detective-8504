# Mission 6 — Git and GitHub

## 1. Task / objective
The objective of this mission was to master core distributed version control operations using Git and GitHub: tracking file states, staging and committing changes, isolating feature development within a dedicated branch (`update-about`), opening a Pull Request (PR) on GitHub, adhering to the instructor's conditional merge instructions, synchronizing changes back to the local `main` branch, and creating a comprehensive Git command glossary.

## 2. Work completed
- Inspected repository status and history using `git status` and `git log`.
- Created and checked out a dedicated feature branch named `update-about`.
- Updated root `README.md` to add a new `My Learning` section documenting key insights from prior missions.
- Staged and committed the documentation update on branch `update-about`.
- Pushed the feature branch to GitHub: `https://github.com/priince0/digital-detective-8504/tree/update-about`.
- Created Pull Request #2 (`https://github.com/priince0/digital-detective-8504/pull/2`) comparing `update-about` against `main`.
- Adhered strictly to the conditional merge rule in Task 6.3 Step 5 by leaving the active Pull Request **OPEN** on GitHub for instructor review.
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
- **Change committed:** Added and refined `My Learning` section in root `README.md`.
- **Pull Request Details:**
  - **PR Number:** Pull Request #2
  - **PR Title:** Update My Learning section with network and workflow takeaways
  - **PR Link:** `https://github.com/priince0/digital-detective-8504/pull/2`
  - **PR Status:** **OPEN / Unmerged** (Active and visible on GitHub)

**Instructor Condition & Catch (Task 6.3 Step 5 & Page 10):**
The assignment instructions explicitly specify:
> *"5. Review the changed file. Merge the PR only if your instructor has asked you to complete the merge."*  
> *"The branch and Pull Request activity must be visible on GitHub. If the PR is not merged, clearly state its status in your README."*

Because the instructor has not yet conducted the lab review or given explicit instruction to merge, **Pull Request #2 has deliberately been kept OPEN and unmerged** on GitHub. This allows the instructor to inspect the open PR diff, branch comparison, and commit trail directly in the GitHub web interface during assignment evaluation. Once the instructor reviews the PR and requests the merge, it can be merged with one click on GitHub, followed by running `git checkout main && git pull origin main` locally as practiced in Step 6.

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
Understanding the conditional requirement in Step 5: *'Merge the PR only if your instructor has asked you to complete the merge. If the PR is not merged, clearly state its status in your README.'*

## 6. How I resolved them
Identified that merging the PR prematurely without instructor approval would remove the active open PR from GitHub's Pull Request review tab. Therefore, left Pull Request #2 open and explicitly stated its unmerged status in this README for instructor inspection.

## 7. Evidence / files
- Mission 6 documentation: `mission-06-git-github/README.md`
- Published branch: `update-about`
- Open Pull Request: `https://github.com/priince0/digital-detective-8504/pull/2` (Status: OPEN)

## 8. Commit details
- **Commit message:** `Document instructor PR status in Mission 6`
- **Branch:** `main`
- **Push status:** Pushed to `https://github.com/priince0/digital-detective-8504.git`
