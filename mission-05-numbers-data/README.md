# Mission 5 — Numbers and data

## 1. Task / objective
The goal of this mission was to learn how computers represent numbers and letters using bits and bytes. I practiced converting numbers by hand between decimal, binary, and hexadecimal, verified my answers using Python in Terminal, built an interactive Python program (`number_converter.py`), and learned about text encoding standards like ASCII and UTF-8.

## 2. Work completed
- Calculated seven number conversions by hand showing the step-by-step math.
- Checked all my answers using Python's built-in functions (`bin()`, `hex()`, and `int()`).
- Wrote `number_converter.py` in Python to convert any entered decimal number into binary and hexadecimal.
- Ran and tested the program with three different positive numbers (13, 42, 255).
- Looked up the ASCII codes for 'A' and 'a', explained why computers need text encoding, and gave an example of a symbol outside basic ASCII.

## 3. Commands / tools used
- Python 3 interactive shell in Terminal (`python3`).
- Built-in Python functions: `bin()`, `hex()`, `int()`, `input()`, `print()`, and `ord()`.
- Running the program: `python3 mission-05-numbers-data/number_converter.py`.

## 4. My understanding

### Task 5.1 — Convert numbers by hand

| Question | Your working and answer |
| :--- | :--- |
| **Convert decimal 13 to binary.** | Dividing by 2 repeatedly:<br>• 13 ÷ 2 = 6, remainder 1<br>• 6 ÷ 2 = 3, remainder 0<br>• 3 ÷ 2 = 1, remainder 1<br>• 1 ÷ 2 = 0, remainder 1<br>Reading remainders from bottom to top: **`1101₂`** |
| **Convert decimal 25 to binary.** | Dividing by 2 repeatedly:<br>• 25 ÷ 2 = 12, remainder 1<br>• 12 ÷ 2 = 6, remainder 0<br>• 6 ÷ 2 = 3, remainder 0<br>• 3 ÷ 2 = 1, remainder 1<br>• 1 ÷ 2 = 0, remainder 1<br>Reading remainders from bottom to top: **`11001₂`** |
| **Convert binary 1010 to decimal.** | Adding positional values (powers of 2):<br>• (1 × 2³) + (0 × 2²) + (1 × 2¹) + (0 × 2⁰)<br>= (1 × 8) + (0 × 4) + (1 × 2) + (0 × 1)<br>= 8 + 0 + 2 + 0 = **`10₁₀`** |
| **Convert binary 1101 to decimal.** | Adding positional values:<br>• (1 × 2³) + (1 × 2²) + (0 × 2¹) + (1 × 2⁰)<br>= (1 × 8) + (1 × 4) + (0 × 2) + (1 × 1)<br>= 8 + 4 + 0 + 1 = **`13₁₀`** |
| **Convert hexadecimal A to decimal.** | In base 16, letters are used for values 10 to 15.<br>• A = 10.<br>• (10 × 16⁰) = **`10₁₀`** |
| **Convert hexadecimal 1F to decimal.** | Adding positional values (powers of 16):<br>• (1 × 16¹) + (F × 16⁰)<br>= (1 × 16) + (15 × 1)<br>= 16 + 15 = **`31₁₀`** |
| **Convert binary 1111 to hexadecimal.** | In binary, 1111 = 8 + 4 + 2 + 1 = 15.<br>• In hexadecimal, 15 is written as **`F₁₆`** (or `0xF`). |

---

### Task 5.2 — Verify using Python

| Test expression | Python output | Matches manual calculation? |
| :--- | :--- | :--- |
| `bin(13)` | `'0b1101'` | Yes |
| `bin(25)` | `'0b11001'` | Yes |
| `int('1010', 2)` | `10` | Yes |
| `int('1101', 2)` | `13` | Yes |
| `int('A', 16)` | `10` | Yes |
| `int('1F', 16)` | `31` | Yes |
| `hex(0b1111)` | `'0xf'` | Yes |

---

### Task 5.3 — Build a small number converter
I wrote a Python program called `number_converter.py` that asks the user to type in a decimal number, converts it to binary and hexadecimal, and prints both.

**Test outputs:**

| Test number | Binary output | Hexadecimal output |
| :--- | :--- | :--- |
| `13` | `0b1101` | `0xd` |
| `42` | `0b101010` | `0x2a` |
| `255` | `0b11111111` | `0xff` |

**What the functions do:**
- `bin(number)`: Converts an integer into a binary string that starts with `0b`. It shows how the number looks in base 2 using only 0s and 1s.
- `hex(number)`: Converts an integer into a hexadecimal string that starts with `0x`. It represents the number in base 16 using digits 0–9 and letters a–f.

---

### Task 5.4 — How is text stored?
- **ASCII decimal codes:**
  - Uppercase `A`: `65` (in binary: `01000001`)
  - Lowercase `a`: `97` (in binary: `01100001`)
- **Why a computer needs an encoding standard:**
  Computers only understand numbers (bits of 0 and 1) and cannot store letters directly. An encoding standard gives every letter and symbol a specific number so that when I type text, the computer can store it in binary and show the exact same letters on any other screen.
- **Example of a character not in basic ASCII:**
  The Indian Rupee symbol (`₹`) or the Euro symbol (`€`). Basic ASCII only has 128 characters for standard English letters and numbers, so other currency symbols and languages need modern standards like UTF-8.

## 5. Difficulties faced
Getting used to reading remainders from bottom to top when converting decimal to binary.

## 6. How I resolved them
I practiced writing the division steps neatly on paper and double-checked the answers in Python using `bin()`.

## 7. Evidence / files
- Mission 5 documentation: `mission-05-numbers-data/README.md`
- Python converter script: `mission-05-numbers-data/number_converter.py`

## 8. Commit details
- **Commit message:** `Build number converter and practise data representation`
- **Branch:** `main`
- **Push status:** Pushed to GitHub
