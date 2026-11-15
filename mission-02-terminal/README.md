# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
The objective of this mission was to develop proficiency in command-line operations: navigating directory trees, listing files with varying levels of detail, safely creating, copying, renaming, and reading files, chaining commands using pipes and flags, and inspecting the local package manager.

## 2. Work completed
- Performed foundational navigation and inspection commands (`pwd`, `ls`, `ls -l`, `cd ..`).
- Created a safe practice folder `terminal-practice/` inside the assignment directory.
- Created `notes.txt`, appended text to it using redirection without overwriting, created a backup copy, and renamed the backup.
- Examined the impact of flags (`-l`, `-a`, `-h`) on directory listings and piped detailed output into `head -n 5`.
- Inspected the installed Homebrew package manager version and reviewed managed packages without making modifications.
- Recorded all observations and conceptual explanations in this README.

## 3. Commands / tools used
- `pwd`: Prints the current working directory path.
- `ls`: Lists files and directories in the current folder.
- `ls -l`: Lists items in long format showing file permissions, owner, size, and timestamp.
- `ls -lah`: Combines flags for long format (`-l`), hidden files (`-a`), and human-readable sizes (`-h`).
- `cd ..`: Moves up one level in the directory hierarchy to the parent folder.
- `mkdir`: Creates a new directory.
- `echo "..." > file`: Writes and redirects output into a file, overwriting existing content.
- `echo "..." >> file`: Appends text to the end of a file preserving existing content.
- `cp`: Copies a file from source to target.
- `mv`: Moves or renames a file or directory.
- `cat`: Concatenates and displays file contents in the terminal.
- `|` (Pipe): Streams stdout from the left command into stdin of the right command.
- `head -n 5`: Filters input to display only the first 5 lines.
- `brew --version` & `brew list`: Checks Homebrew package manager details.

## 4. My understanding

### Task 2.1 — Basic Terminal operations

| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display (`pwd`)** | Prints the full absolute path of the present working directory. | Returned `/Users/[redacted]/Desktop/digital-detective-8504`. |
| **Directory listing (`ls`)** | Lists names of visible files and folders in alphabetical order. | Displayed mission folders, `README.md`, and `evidence`. |
| **Detailed listing (`ls -l`)** | Shows detailed file attributes (permissions, links, user, group, byte size, date, name). | Columns for file permissions (e.g. `-rw-r--r--`), size in bytes, and last modified date. |
| **Change directory (`cd ..`)** | Changes the shell session working directory to the parent folder. | Moved up one level to `/Users/[redacted]/Desktop`. Running `cd digital-detective-8504` returned back. |
| **Create directory (`mkdir practice`)** | Creates a new subfolder in the specified location. | Created folder `practice/` without error. |
| **Create empty file (`touch practice/sample.txt`)** | Creates an empty file or updates the timestamp of an existing file. | Created `sample.txt` with size 0 bytes. |
| **Copy file (`cp practice/sample.txt practice/sample_copy.txt`)** | Creates an identical duplicate file at the target path. | Both `sample.txt` and `sample_copy.txt` existed independently. |
| **Move / rename file (`mv practice/sample_copy.txt practice/sample_renamed.txt`)** | Renames or moves a file to a new location. | `sample_copy.txt` was renamed to `sample_renamed.txt`; original copy name no longer existed. |
| **Display file contents (`cat practice/sample.txt`)** | Reads and prints the entire content of a file to stdout. | Printed the text content directly into the terminal window. |

---

### Task 2.2 — Practise file changes safely
Completed in `terminal-practice/`:
1. Created `notes.txt` with: `Initial line of test notes.`
2. Appended second line with `>>`: `Appended second line of test notes.`
3. Verified using `cat notes.txt`:
   ```
   Initial line of test notes.
   Appended second line of test notes.
   ```
4. Backed up using `cp notes.txt notes_backup.txt` and renamed using `mv notes_backup.txt notes_backup_archive.txt`.

**Answers to questions:**
- **Difference between replacing and adding text:**
  Using the single redirection operator (`>`) overwrites the target file entirely, truncating existing data and replacing it with the new input. Using the append operator (`>>`) preserves existing file data and appends the new text directly to the end of the file.
- **Difference between copying and moving:**
  Copying (`cp`) duplicates the file so that two separate instances exist on disk; modifications to one do not affect the other. Moving (`mv`) relocates or renames the file reference in the file system metadata without duplicating data blocks, leaving only a single file at the new path or name.
- **What information current-directory display provides:**
  `pwd` provides the absolute canonical path from the root directory (`/`) to the folder currently being accessed by the active shell session, preventing accidental modifications in unintended folders.
- **Why a directory-listing operation is useful:**
  `ls` gives immediate visibility into existing files, subdirectories, hidden configuration files, file sizes, and write timestamps before issuing destructive commands or navigating further.

---

### Task 2.3 — Understand flags and pipes
- **Comparison between `ls` and `ls -lah`:**
  A basic `ls` only prints the file and folder names horizontally. In contrast, `ls -lah` modifies the command behavior:
  - `-l`: Formats output as a long detailed list showing permissions, ownership, size, and date.
  - `-a`: Includes hidden files (entries starting with `.`, such as `.git` and `.gitkeep`).
  - `-h`: Formats file sizes into human-readable units (e.g. `128B`, `4.2K`, `2.5M`) rather than raw byte counts.
- **Pipes (`|`):**
  Running `ls -la terminal-practice | head -n 5` redirects the standard output (stdout) of `ls -la` directly into the standard input (stdin) of `head -n 5`. The left command produces the full multi-line directory listing, and the right command filters and emits only the first 5 lines.

---

### Task 2.4 — Understand package managers
- **Homebrew Inspection:**
  - Command: `brew --version`
  - Observation: `Homebrew 7.0.9`
  - Command: `brew list`
  - Observation: Installed packages include developer tools and libraries such as `node`, `git`, `ffmpeg`, `htop`, `openssl@3`, and `sqlite`.
- **Why package managers are useful:**
  A package manager automates the installation, updating, dependency resolution, and uninstallation of software packages from the command line. Instead of manually downloading installers, configuring build flags, and tracking library dependencies, a single command reliably pulls verified packages and keeps software up to date.

## 5. Difficulties faced
Care had to be taken when demonstrating append vs overwrite redirection to ensure the original line was not accidentally destroyed by an errant `>` operator.

## 6. How I resolved them
Verified the command syntax (`>>` for append) and confirmed the resulting file contents with `cat` before moving to the backup and rename steps.

## 7. Evidence / files
- Mission 2 documentation: `mission-02-terminal/README.md`
- Practice workspace: `terminal-practice/notes.txt`
- Renamed archive file: `terminal-practice/notes_backup_archive.txt`

## 8. Commit details
- **Commit message:** `Complete Terminal and file management mission`
- **Branch:** `main`
- **Push status:** Pushed to `https://github.com/priince0/digital-detective-8504.git`
