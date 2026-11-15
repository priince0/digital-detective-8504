# Mission 4 — How programs run

## 1. Task / objective
The objective of this mission was to create and execute a standalone Python script from the command line, observe its runtime execution, and conduct a comparative analysis between compiled and interpreted programming language execution models.

## 2. Work completed
- Created the Python source file `hello.py` inside `mission-04-programs/`.
- Wrote a single-line Python program displaying `Hello from Python`.
- Executed the program using `python3 mission-04-programs/hello.py` and confirmed output in the terminal.
- Completed the compiler versus interpreter comparison table and detailed conceptual summary.

## 3. Commands / tools used
- `python3 mission-04-programs/hello.py`: Invoked the Python 3 interpreter to parse and execute the script.
- Terminal output observation.

## 4. My understanding

### Task 4.1 — Program execution
- Program file: `hello.py`
- Source code:
  ```python
  print("Hello from Python")
  ```
- Command executed:
  ```bash
  python3 mission-04-programs/hello.py
  ```
- Terminal Output:
  ```
  Hello from Python
  ```

---

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | Translates the entire source code into machine code or intermediate binary prior to program execution in a separate build step. | Translates and executes instructions on-the-fly line-by-line or statement-by-statement at runtime. |
| **Typical output** | Produces a standalone executable binary file (e.g., `.exe` or ELF/Mach-O binary) or bytecode file. | Directly produces execution results and console output in memory without creating a permanent standalone machine binary. |
| **One example** | C, C++, Rust, or Go compilers (such as `clang` or `gcc`). | Python (`CPython`), Ruby, or JavaScript (in simple shell environments). |
| **One advantage** | Maximum runtime performance and execution speed because optimization happens ahead of time and the CPU executes native machine instructions directly. | Rapid development and debugging turnaround, as code can be edited and tested immediately without waiting for a compilation phase. |

**Summary explanation:**
A compiler takes high-level source code and translates the entire program all at once into standalone native machine code before execution begins. Once compiled, the resulting executable runs directly on the CPU hardware at high speed without needing the original compiler. In contrast, an interpreter processes source code or bytecode line-by-line during runtime, translating each instruction as it encounters it. While compiled code executes much faster, interpreted languages provide greater portability across platforms and an immediate interactive feedback loop for developers.

## 5. Difficulties faced
Understanding how modern languages like Python blend both models by first compiling source code into `.pyc` bytecode before executing it inside a virtual machine interpreter.

## 6. How I resolved them
Clarified that although Python generates intermediate bytecode, it is still classified primarily as an interpreted language because the bytecode is executed dynamically by the CPython virtual machine at runtime rather than compiled into standalone native CPU machine instructions.

## 7. Evidence / files
- Mission 4 documentation: `mission-04-programs/README.md`
- Source file: `mission-04-programs/hello.py`

## 8. Commit details
- **Commit message:** `Compare compilers and interpreters`
- **Branch:** `main`
- **Push status:** Pushed to `https://github.com/priince0/digital-detective-8504.git`
