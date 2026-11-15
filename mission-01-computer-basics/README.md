# Mission 1 — Know your computer

## 1. Task / objective
The objective of this mission was to analyze the fundamental Input-Process-Output-Storage (IPOS) cycle of a computer system, trace a concrete user activity through every stage, classify key hardware and software components (operating system, application, and utility software), and examine specialized computer systems encountered in daily life.

## 2. Work completed
- Selected the activity of typing and saving a programming assignment document to trace through the IPOS model.
- Completed the IPOS activity trace table detailing the actions and components at each stage.
- Compiled a hardware and software classification table listing four hardware devices and four software tools with their categories and functions.
- Analyzed three everyday computer systems (Automated Teller Machine, Smart TV, and Automated Traffic Light System).
- Documented all findings and reflections in this README.

## 3. Commands / tools used
- Text Editor (VS Code) for drafting documentation and markdown tables.
- System Information (`system_profiler` / Activity Monitor) to inspect physical hardware components installed on the computer.

## 4. My understanding

### Task 1.1 — Trace one activity using IPOS
**Chosen Activity:** Writing Python code in a text editor and saving the script to disk.

| Stage | What happens in your example? | Possible hardware / component |
| :--- | :--- | :--- |
| **Input** | The user presses keys on the keyboard to enter Python code, and clicks 'Save' using the trackpad/mouse. Keystrokes generate electrical signals sent to the controller. | Keyboard, Trackpad / Mouse |
| **Processing** | The CPU accepts input interrupts, retrieves character codes, updates application memory (RAM), executes editor logic, and prepares data blocks for disk write. | CPU (Processor) and RAM (Memory) |
| **Output** | The display controller and screen refresh pixels to immediately render the typed code characters and display the file status indicators. | Retina Display / Monitor |
| **Storage** | When the save command triggers, the file system writes the bytes permanently from temporary RAM into non-volatile NAND flash blocks on the SSD. | Solid State Drive (SSD) |

**Detailed Flow:**
The activity begins with the user providing input through keystrokes on the physical keyboard. Each keystroke sends an electrical interrupt to the operating system, which hands the event to the active text editor process. The CPU processes this input by mapping the key codes to Unicode/ASCII characters and storing them in working RAM memory. Concurrently, the GPU and display engine output the rendered characters visually onto the monitor so the user can verify their input. When the save shortcut is invoked, the CPU coordinates with the operating system storage driver to serialize the memory buffer into permanent blocks on the local SSD, ensuring data persistence even when the computer powers off.

---

### Task 1.2 — Identify hardware and software

| Item / software name | Hardware or software? | Software type (if applicable) | Purpose |
| :--- | :--- | :--- | :--- |
| **Keyboard** | Hardware | Not applicable | Mechanical/membrane input device used to enter alphanumeric characters and commands. |
| **Retina Display / Monitor** | Hardware | Not applicable | Primary visual output device used to render text, graphics, and user interfaces. |
| **Apple M-Series CPU** | Hardware | Not applicable | Central processing unit that fetches, decodes, and executes program instructions. |
| **Internal NVMe SSD** | Hardware | Not applicable | High-speed non-volatile secondary storage for the operating system, applications, and files. |
| **macOS (Darwin)** | Software | Operating system software | Manages system hardware, schedules processes, manages memory, and provides file system APIs. |
| **Visual Studio Code** | Software | Application software | Integrated development environment used for writing code, editing text, and managing projects. |
| **Google Chrome** | Software | Application software | Web browser used to access web applications, documentation, and web services. |
| **macOS Terminal / zsh** | Software | Utility software | Command-line utility that allows users to interact directly with the shell and file system. |

---

### Task 1.3 — Computer systems around you

| System | Main purpose | One input | One output |
| :--- | :--- | :--- | :--- |
| **ATM (Automated Teller Machine)** | Securely processes banking transactions such as cash withdrawals and balance inquiries. | Keypad / Touchscreen (PIN and withdrawal amount entered by user) or Card Reader chip scan. | Cash dispenser releasing bank notes and Receipt printer / Screen confirmation. |
| **Smart TV** | Receives, decodes, and streams digital multimedia content and running streaming apps. | Infrared / Bluetooth remote control button presses or voice microphone input. | High-definition display panel displaying video and built-in speakers producing audio. |
| **Automated Traffic Light System** | Controls the flow of vehicular and pedestrian traffic at road intersections based on timers or sensors. | Induction loop sensor embedded in the road detecting vehicles or pedestrian push button. | Colored LED signal lamps (Red, Yellow, Green) directing traffic. |

## 5. Difficulties faced
Differentiating strictly between utility software and application software can be subtle, particularly for built-in tools like Terminal or Activity Monitor.

## 6. How I resolved them
Reviewed the definitions: application software serves a primary user-oriented productivity/entertainment task, whereas utility software assists in optimizing, configuring, monitoring, or maintaining system resources and low-level operations.

## 7. Evidence / files
- Mission 1 documentation: `mission-01-computer-basics/README.md`

## 8. Commit details
- **Commit message:** `Complete computer basics and IPOS mission`
- **Branch:** `main`
- **Push status:** Pushed to `https://github.com/priince0/digital-detective-8504.git`
