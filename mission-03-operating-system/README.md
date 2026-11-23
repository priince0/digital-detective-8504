# Mission 3 — Understand the operating system

## 1. Task / objective
The goal of this mission was to check my operating system details, see what processes are currently running on my computer, understand process IDs (PIDs), learn the difference between absolute and relative file paths, check file permissions, and explain the main jobs of an operating system.

## 2. Work completed
- Checked my macOS version, user account, free disk storage, and active CPU usage using terminal commands.
- Looked at the running process list to understand what a process is and what the PID column means.
- Compared absolute and relative paths using files in my project.
- Checked file permissions on `terminal-practice/notes.txt` to see who can read, write, or execute it.
- Wrote down the main responsibilities of an operating system with simple everyday examples.

## 3. Commands / tools used
- `sw_vers`: Showed the macOS name and version number.
- `whoami`: Showed the user account currently logged into the terminal.
- `df -h /`: Showed the total, used, and available disk storage on my computer.
- `top -l 1`: Took a snapshot of system activity, CPU usage, and running processes.
- `ps -Ao pid,comm,%cpu,%mem`: Listed running processes with their PID and memory/CPU percentages.
- `ls -l`: Checked the file permissions and ownership of my test files.

## 4. My understanding

### Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** | Tells me the exact name and release version of the OS running on my laptop. | `macOS 27.2.1` |
| **Current account identity** | Tells me which user account owns the current terminal session. | `[redacted]` |
| **Available and used storage** | Shows how much total storage space the disk has, how much is taken up, and how much is free. | Disk size: `460 GiB`, Used: `13 GiB`, Available: `306 GiB` |
| **System activity snapshot** | Gives a real-time look at how hard the CPU and memory are working. | 876 total processes, CPU usage: ~5.6% user, ~9.0% system, ~85.4% idle |

---

### Task 3.2 — Understand processes
- **What is a process?**  
  A process is simply a program that is currently running on the computer. When you open an application or run a script, the operating system creates a process for it in memory.
- **What does the PID column represent?**  
  PID stands for Process Identifier. It is a unique number that the operating system assigns to every running process so it can keep track of them individually.
- **Two examples of running processes:**  
  1. `/sbin/launchd` (PID 1): A background system service that starts when macOS boots and manages other system tasks.  
  2. `Google Chrome` (or `Visual Studio Code`): An application process running when I open my browser or code editor.

---

### Task 3.3 — Understand paths and permissions
- **Navigating between folders:**  
  When I ran `pwd` inside the assignment root, it showed `/Users/[redacted]/Desktop/digital-detective-8504`. After running `cd mission-00-setup` and `pwd`, the location updated to `/Users/[redacted]/Desktop/digital-detective-8504/mission-00-setup`. Running `cd ..` brought me back up.
- **Absolute vs Relative paths:**
  - An **absolute path** gives the complete directions to a file starting from the very top root folder (`/`). It always works no matter where you currently are in the terminal.
    - Example: `/Users/[redacted]/Desktop/digital-detective-8504/mission-00-setup/README.md`
  - A **relative path** starts from the folder you are currently sitting in (`.`).
    - Example: `mission-00-setup/README.md` (when I am in the project root folder) or `../README.md` (if I am inside a subfolder).
- **File permissions check:**  
  When I checked `terminal-practice/notes.txt` with `ls -l`, the permission string was `-rw-r--r--`:
  - The first letter `-` means it is a regular file.
  - The next three letters `rw-` are the permissions for the owner:
    - `r` (read): I can open and read the file.
    - `w` (write): I can edit or save changes to the file.
    - `-` (no execute): It is just a text file, not a runnable program, so it does not have execute permission.

| Permission | Meaning | Example |
| :--- | :--- | :--- |
| **r — Read** | Lets you open and view the content of a file. | Opening a text file to read it with `cat`. |
| **w — Write** | Lets you change, add text to, or edit a file. | Saving new lines of code in a file. |
| **x — Execute** | Lets you run the file as a program or script. | Running a Python script or shell script. |

---

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | Decides which programs get to use the CPU and keeps them running smoothly without crashing each other. | Running a web browser, Spotify, and a code editor at the same time. |
| **Memory management** | Gives RAM space to programs when they open and takes it back when they close. | Giving 500 MB of RAM to a browser tab when it opens. |
| **Device management** | Helps the computer communicate with connected hardware like mice, printers, and screens. | Detecting when I plug in a USB mouse and moving the cursor. |
| **File management** | Organizes files into folders on the disk so you can easily save, find, and delete them. | Creating a folder on the desktop and saving notes inside it. |
| **User interface / shell** | Gives you a way to interact with the computer, either through clickable windows (GUI) or typed commands (Terminal). | Using the Terminal (`zsh`) or the graphical macOS desktop. |
| **Security and permissions** | Keeps files safe by checking who is allowed to open, edit, or delete them. | Asking for an admin password before installing new software. |

## 5. Difficulties faced
Understanding the difference between the full path and the relative path when moving between folders.

## 6. How I resolved them
I used `pwd` to see where I was before running `cd`, and practiced using `..` to move back up one level.

## 7. Evidence / files
- Mission 3 documentation: `mission-03-operating-system/README.md`

## 8. Commit details
- **Commit message:** `Document operating system and file management`
- **Branch:** `main`
- **Push status:** Pushed to GitHub
