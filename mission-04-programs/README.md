# Mission 4 — How programs run

## 1. Task / objective
The goal of this mission was to write and run a simple Python script from the terminal, see the output, and learn the main differences between how compilers and interpreters run code.

## 2. Work completed
- Created a file named `hello.py` inside the `mission-04-programs/` folder.
- Wrote a one-line Python script that prints `Hello from Python`.
- Ran the script from Terminal using `python3 mission-04-programs/hello.py` and saw the printed message.
- Made a comparison table between compilers and interpreters, and explained the differences in my own words.

## 3. Commands / tools used
- `python3 mission-04-programs/hello.py`: Used Python 3 to run the script.
- Terminal to view the output.

## 4. My understanding

### Task 4.1 — Create and run a Python program
- File name: `hello.py`
- Program code:
  ```python
  print("Hello from Python")
  ```
- Terminal command:
  ```bash
  python3 mission-04-programs/hello.py
  ```
- Output:
  ```
  Hello from Python
  ```

---

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | Translates the whole program all at once into machine code before the program starts running. | Translates and runs the code line by line while the program is running. |
| **Typical output** | Produces a separate executable file (like a `.exe` file or runnable binary). | Does not produce an executable file; it just runs the code in memory and shows the results. |
| **One example** | C or C++ | Python |
| **One advantage** | Programs usually run faster because all the translation was already done ahead of time. | It is easier and quicker to write and test code because you can run your changes immediately without having to compile first. |

**Explanation in my own words:**  
A compiler takes your entire code and translates all of it into machine code before you can run it. Because the computer can understand the compiled file directly, the program runs very fast. An interpreter, on the other hand, reads your code line by line at runtime and carries out the instructions as it goes. Even though interpreted programs can run a bit slower, they are much friendlier for beginners because you can test and fix your code instantly.

## 5. Difficulties faced
Understanding whether Python compiles anything before running it.

## 6. How I resolved them
I learned that even though Python converts code into bytecode behind the scenes, it is still considered an interpreted language because the Python interpreter executes that code line by line while the program is running.

## 7. Evidence / files
- Mission 4 documentation: `mission-04-programs/README.md`
- Python file: `mission-04-programs/hello.py`

## 8. Commit details
- **Commit message:** `Compare compilers and interpreters`
- **Branch:** `main`
- **Push status:** Pushed to GitHub
