# Mission 3 — Understand the operating system

## 1. Task / objective
The objective of this mission was to inspect the host operating system environment, explore active processes and system metrics, distinguish between absolute and relative file paths, examine POSIX file permission models, and document the core architectural responsibilities of an operating system.

## 2. Work completed
- Checked the operating system version, active user account identity, available disk storage, and real-time CPU/memory activity using terminal utilities.
- Examined the process table to understand Process Identifiers (PIDs) and background daemon/application tasks.
- Navigated directory hierarchies to contrast absolute versus relative path notation using project files.
- Analyzed file permission strings (`r`, `w`, `x`) for files in the practice folder.
- Completed the operating system core responsibilities analysis table with real-world examples.

## 3. Commands / tools used
- `sw_vers`: Reports operating system product name and release version.
- `whoami`: Displays the username of the active terminal session.
- `df -h /`: Displays disk filesystem capacity, used space, and available storage in human-readable gigabytes.
- `top -l 1`: Generates a single-frame system snapshot of CPU, memory, and thread utilization.
- `ps -Ao pid,comm,%cpu,%mem`: Lists running processes with their PID, command name, CPU percentage, and memory usage.
- `ls -l`: Inspects file permissions, ownership, and metadata.

## 4. My understanding

### Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** | The exact name, kernel build, and release version of the operating system running on the machine. | `macOS 27.2.1` (Apple Darwin kernel on ARM64 architecture). |
| **Current account identity** | The specific user account that owns the active shell session and determines privilege scope. | Active account: `[redacted]` (standard non-root user). |
| **Available and used storage** | Total disk capacity, space consumed by files, and remaining free space on the root filesystem. | Filesystem size: `460 GiB`, Used: `13 GiB` (system volume), Available: `306 GiB` (~5% capacity used on root volume). |
| **System activity snapshot** | Real-time state of hardware resources: active threads, CPU idle/user percentages, and physical RAM distribution. | 876 total processes (2 running, 874 sleeping), CPU usage: ~5.6% user, ~9.0% system, ~85.4% idle; 15 GiB physical memory utilized. |

---

### Task 3.2 — Understand processes
- **What is a process?**
  A process is an instance of a computer program currently in execution. It contains the program code, its current execution state (program counter and registers), allocated virtual memory address space (stack and heap), and operating system resource handles (open file descriptors and network sockets).
- **What does the PID column represent?**
  The PID (Process Identifier) is a unique non-negative integer assigned by the operating system kernel to identify and track each active process throughout its lifetime.
- **Two examples of running processes:**
  1. `/sbin/launchd` (PID 1): The root init daemon in macOS responsible for bootstrapping the user space and managing system services.
  2. `zsh` (Shell process): The interactive command line interpreter process currently executing terminal sessions.

---

### Task 3.3 — Understand paths and permissions
- **Difference between absolute and relative paths:**
  - An **absolute path** specifies the full location of a file or directory starting unconditionally from the root directory (`/`). It is independent of the shell's current location.
    - Example: `/Users/[redacted]/Desktop/digital-detective-8504/mission-00-setup/README.md`
  - A **relative path** specifies the location of a target file or directory relative to the current working directory (`.`).
    - Example: `mission-00-setup/README.md` (when working from the repository root) or `../README.md` (when inside a subfolder).
- **File Permissions Analysis:**
  Inspected file: `terminal-practice/notes.txt`
  Output string: `-rw-r--r--`
  - The leading `-` indicates a regular file.
  - The first triad `rw-` represents the **owner permissions**:
    - `r` (read): The owner has permission to open and read file contents.
    - `w` (write): The owner has permission to edit, append to, or modify the file.
    - `-` (no execute): The file cannot be executed as a program.
  - The second and third triads (`r--`, `r--`) represent group and others permissions (read-only).

| Permission | Meaning | Example |
| :--- | :--- | :--- |
| **r — Read** | Allows a file's contents to be read or a directory's entries to be listed. | Opening and reading a text document or using `cat`. |
| **w — Write** | Allows a file to be modified or saved, and items to be added/removed in a folder. | Editing and saving Python code in an editor. |
| **x — Execute** | Allows a file to be executed as a binary/script, or allows entering a directory. | Running a shell script (`./script.sh`) or `cd` into a directory. |

---

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | Schedules running programs on available CPU cores, handles multitasking, and manages process creation and termination. | Switching execution between a web browser, code editor, and music player using time-slicing. |
| **Memory management** | Allocates and tracks physical RAM addresses for active programs while isolating process memory spaces via virtual memory. | Allocating 200 MB of RAM when opening a document and freeing it when the application is closed. |
| **Device management** | Communicates with hardware peripherals using specialized device drivers and manages input/output requests. | Translating USB/Bluetooth mouse movement and keyboard keystrokes into OS input events. |
| **File management** | Organizes, stores, retrieves, and protects files in a structured hierarchical file system on storage drives. | Creating, saving, renaming, and reading files inside folders on an APFS or ext4 filesystem. |
| **User interface / shell** | Provides a visual GUI or command-line CLI interface allowing users and applications to interact with the system. | Providing the terminal command shell (`zsh`) or graphical desktop windows and menus. |
| **Security and permissions** | Enforces access controls, user authentication, privilege boundaries, and file permissions to protect data. | Preventing standard user accounts from modifying protected root system files without authorization. |

## 5. Difficulties faced
Understanding the distinction between virtual memory size (VSIZE) and actual resident physical memory (RES/MEM) displayed in terminal process tables.

## 6. How I resolved them
Reviewed how the kernel uses virtual paging: VSIZE reflects total mapped address space, whereas resident memory reflects the physical RAM pages currently occupied.

## 7. Evidence / files
- Mission 3 documentation: `mission-03-operating-system/README.md`

## 8. Commit details
- **Commit message:** `Document operating system and file management`
- **Branch:** `main`
- **Push status:** Pushed to `https://github.com/priince0/digital-detective-8504.git`
