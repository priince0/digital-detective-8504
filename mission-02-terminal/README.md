# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
The goal of this mission was to get comfortable using the command line (Terminal). I practiced navigating folders, listing files with different options, safely creating, copying, renaming, and viewing text files, chaining commands using pipes, and checking my package manager.

## 2. Work completed
- Practiced the basic terminal commands (`pwd`, `ls`, `ls -l`, `cd ..`, `mkdir`, `touch`, `cp`, `mv`, `cat`).
- Created a safe practice folder called `terminal-practice/` inside the project.
- Created `notes.txt`, added text to it, appended another line without deleting the first line, made a backup, and renamed the backup.
- Looked at how flags change command outputs (`ls` vs `ls -lah`) and tested piping output into `head -n 5`.
- Checked my Homebrew package manager version and saw what packages are installed.
- Documented my findings and answers to the questions below.

## 3. Commands / tools used
- `pwd`: Shows the full path of the current folder I am in.
- `ls`: Lists files and folders in the current directory.
- `ls -l`: Shows a detailed list with file permissions, sizes, and dates.
- `ls -lah`: Lists all files (including hidden ones) with sizes in KB/MB.
- `cd ..`: Moves up to the parent directory.
- `mkdir`: Creates a new folder.
- `echo "..." > file`: Writes text into a file (overwrites anything already there).
- `echo "..." >> file`: Appends text to the end of a file without erasing what was there.
- `cp`: Makes a copy of a file.
- `mv`: Moves or renames a file.
- `cat`: Shows the contents of a file in the terminal.
- `|` (Pipe): Takes the output from one command and passes it directly into another command.
- `head -n 5`: Shows only the first 5 lines of output.
- `brew --version` & `brew list`: Checks the package manager.

## 4. My understanding

### Task 2.1 — Basic Terminal operations

| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display (`pwd`)** | Prints the full path of the folder I am currently working in. | Displayed `/Users/[redacted]/Desktop/digital-detective-8504`. |
| **Directory listing (`ls`)** | Lists the visible files and folders in the current folder. | Showed all the mission folders and `README.md`. |
| **Detailed listing (`ls -l`)** | Shows detailed information like permissions, owner, byte size, and last modified date. | Displayed extra columns with permissions like `-rw-r--r--` and file size. |
| **Change directory (`cd ..`)** | Moves up one level into the parent directory. | Moved up into my Desktop folder. Running `cd digital-detective-8504` took me right back. |
| **Create directory (`mkdir practice`)** | Creates a new subfolder. | A new folder named `practice` appeared. |
| **Create empty file (`touch practice/sample.txt`)** | Creates a new blank file. | Created `sample.txt` with a file size of 0 bytes. |
| **Copy file (`cp practice/sample.txt practice/sample_copy.txt`)** | Makes a second identical copy of the file. | Both `sample.txt` and `sample_copy.txt` were now present. |
| **Move / rename file (`mv practice/sample_copy.txt practice/sample_renamed.txt`)** | Renames the file or moves it to another folder. | `sample_copy.txt` was renamed to `sample_renamed.txt`. The old name was gone. |
| **Display file contents (`cat practice/sample.txt`)** | Prints the contents of a text file on the screen. | Printed the text inside the file right onto the terminal screen. |

---

### Task 2.2 — Practise file changes safely
I did this practice inside `terminal-practice/`:
1. Created `notes.txt` with: `Initial line of test notes.`
2. Added a second line using `>>`: `Appended second line of test notes.`
3. Ran `cat notes.txt` to verify both lines were there:
   ```
   Initial line of test notes.
   Appended second line of test notes.
   ```
4. Copied the file using `cp notes.txt notes_backup.txt` and then renamed it using `mv notes_backup.txt notes_backup_archive.txt`.

**Questions and Answers:**
- **What is the difference between replacing a file's contents and adding text to the end?**
  When you use `>`, it completely wipes out whatever was in the file before and replaces it with the new text. When you use `>>`, it keeps the existing text and just adds the new line at the very bottom.
- **What is the difference between copying a file and moving a file?**
  Copying (`cp`) makes a duplicate so that you end up with two separate files. Moving (`mv`) just changes where the file is or changes its name, leaving only one file.
- **What information does the current-directory display provide?**
  `pwd` gives the exact location path from the root of the computer to the folder you are in. This helps make sure you don't accidentally edit or delete files in the wrong place.
- **Why is a directory-listing operation useful?**
  `ls` lets you see what files and folders are around before you start opening, editing, or deleting things.

---

### Task 2.3 — Understand flags and pipes
- **Difference between `ls` and `ls -lah`:**
  A basic `ls` just prints file names in simple rows. Adding flags changes what it displays:
  - `-l`: Shows details like permissions, size, and modification date.
  - `-a`: Shows all files, including hidden files that start with a dot (like `.git`).
  - `-h`: Shows file sizes in easy-to-read units like KB and MB instead of raw bytes.
- **Pipes (`|`):**
  When I ran `ls -la terminal-practice | head -n 5`, the pipe symbol `|` took the full list of files produced by `ls -la` and sent it directly into `head -n 5`. The `head` command then printed only the top 5 lines.

---

### Task 2.4 — Understand package managers
- **Checking Homebrew:**
  - Ran `brew --version` and saw `Homebrew 7.0.9`.
  - Ran `brew list` and saw installed tools like `git`, `node`, `htop`, and `sqlite`.
- **Why package managers are useful:**
  A package manager makes it very easy to install, update, and remove software from the command line. Instead of having to search the web for an installer, download it, and set it up manually, you can just run one simple command and it handles everything automatically.

## 5. Difficulties faced
Remembering whether `>` or `>>` was used for appending without erasing the file.

## 6. How I resolved them
I tested it out carefully on a test file and confirmed that `>>` is the one that appends to the end of the file.

## 7. Evidence / files
- Mission 2 documentation: `mission-02-terminal/README.md`
- Practice files: `terminal-practice/notes.txt` and `terminal-practice/notes_backup_archive.txt`

## 8. Commit details
- **Commit message:** `Complete Terminal and file management mission`
- **Branch:** `main`
- **Push status:** Pushed to GitHub
