# Mission 6 — Git and GitHub

## 1. Task / objective
The goal of this mission was to learn how version control works with Git and GitHub. I practiced checking repository status, staging and committing changes, creating a separate branch called `update-about`, opening a Pull Request (PR) on GitHub, understanding the instructor's rule about merging, and building a Git command glossary.

## 2. Work completed
- Used `git status` and `git log` to see untracked files and previous commits.
- Created and switched to a new branch called `update-about`.
- Updated the root `README.md` to add a section called `My Learning` describing what I learned so far.
- Staged and committed the changes on the `update-about` branch.
- Pushed the branch to GitHub: `https://github.com/priince0/digital-detective-8504/tree/update-about`.
- Opened Pull Request #2 on GitHub (`https://github.com/priince0/digital-detective-8504/pull/2`) to compare `update-about` with `main`.
- Followed Step 5 by leaving the Pull Request **OPEN** on GitHub so the instructor can review it.
- Wrote a one-line explanation for each common Git command in the glossary table.

## 3. Commands / tools used
- `git status`: Checks which files are modified or staged.
- `git add <file>`: Stages a file so it can be committed.
- `git commit -m "..."`: Saves the staged changes into the local history.
- `git log --oneline`: Shows a compact list of past commits.
- `git checkout -b update-about`: Creates and switches to a new branch.
- `git push -u origin update-about`: Pushes the new branch to GitHub.
- `git checkout main`: Switches back to the main branch.
- GitHub web interface to view branches and create the Pull Request.

## 4. My understanding

### Task 6.1 — Basic Git workflow

| Git operation | What it does in your own words |
| :--- | :--- |
| **Check repository status** | Shows which files have been modified, which files are ready to be committed, and which are untracked. |
| **Stage selected changes** | Picks specific changed files and gets them ready to be saved in the next commit. |
| **Create a commit** | Saves a permanent snapshot of the staged changes along with a message explaining what was done. |
| **View commit history** | Shows the list of past commits so you can see who changed what and when. |

**Difference between staging and committing:**  
Staging (`git add`) is like putting files into a box before sealing it. You can pick and choose exactly which changes go in. Committing (`git commit`) is like sealing the box and putting a label on it—it permanently records that snapshot into Git's history.

---

### Task 6.2 & 6.3 — Branches and Pull Requests
- **Branch created:** `update-about`
- **Change made:** Added and updated the `My Learning` section in `README.md`.
- **Pull Request details:**
  - **PR Number:** Pull Request #2
  - **PR Title:** Update My Learning section with network and workflow takeaways
  - **PR Link:** `https://github.com/priince0/digital-detective-8504/pull/2`
  - **PR Status:** **OPEN / Unmerged** (waiting for instructor review)

**Instructor note on merging (Step 5):**  
Task 6.3, Step 5 specifically states:  
> *"Merge the PR only if your instructor has asked you to complete the merge. If the PR is not merged, clearly state its status in your README."*

Because my instructor has not yet asked me to merge, I have kept **Pull Request #2 open on GitHub**. This way, my instructor can click on the `Pull requests` tab on GitHub to see the open PR, review the branch comparison, and see the diff before giving instructions to merge it.

**Why branches and Pull Requests are useful:**  
- A **branch** gives you an isolated workspace to try new ideas or work on new features without messing up the working code on `main`.
- A **Pull Request** lets team members review and discuss your changes before anything gets merged into the main project.

---

### Task 6.4 — Git command glossary

| Operation | Command | One-line explanation in my own words |
| :--- | :--- | :--- |
| **Initialise a repository** | `git init` | Starts tracking a folder with Git by creating a hidden `.git` folder. |
| **Check status** | `git status` | Shows which files are modified, staged, or untracked. |
| **Stage changes** | `git add <file>` | Adds changed files to the staging area so they can be committed. |
| **Commit changes** | `git commit -m "<msg>"` | Saves the staged files as a permanent snapshot in history. |
| **View history** | `git log` | Displays past commits with their messages and commit IDs. |
| **Create or list branches** | `git branch` | Lists existing branches or creates a new one. |
| **Switch branches** | `git switch <branch>` | Switches the working directory over to a different branch. |
| **Publish changes** | `git push <remote> <branch>` | Uploads local commits from your computer to GitHub. |
| **Retrieve remote changes** | `git pull <remote> <branch>` | Downloads new changes from GitHub and merges them into your current branch. |

## 5. Difficulties faced
Reading Step 5 carefully to understand whether I should merge the PR right away or wait.

## 6. How I resolved them
I noticed that Step 5 says to merge only if asked by the instructor, so I left the PR open on GitHub and made sure to document its open status here.

## 7. Evidence / files
- Mission 6 documentation: `mission-06-git-github/README.md`
- Branch: `update-about` (visible on GitHub)
- Open Pull Request: `https://github.com/priince0/digital-detective-8504/pull/2`

## 8. Commit details
- **Commit message:** `Complete Git and GitHub collaboration mission`
- **Branch:** `main`
- **Push status:** Pushed to GitHub
