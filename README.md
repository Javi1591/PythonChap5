# Program 5 – Python Modules and Function Design

A multi-file Python project demonstrating modular programming, function design, and inter-module communication.  
Each program builds on the previous one by introducing reusable components, function calls, and parameter passing.

---

## Program 1 – Subtotal Calculator (`nazario5_1.py` + `subtotal.py`)

### Description
A Python program that calculates subtotals for multiple purchased items using a separate module.  
Demonstrates how to import and call external modules for function reuse.

### Features
- Imports a user-defined module named `subtotal`.
- Prompts for item description, price, and quantity.
- Calls the `subtotal()` function for each item to compute individual totals.
- Accumulates and displays formatted purchase information.

### Files
- `nazario5_1.py` — main driver program:contentReference[oaicite:0]{index=0}.  
- `subtotal.py` — module that defines the `subtotal()` function:contentReference[oaicite:1]{index=1}.

### Notes
- Reinforces modular programming and function calls across files.
- Demonstrates formatted numeric output and user input.
- References:  
  - *Python 3 Documentation – Modules and Packages*  
  - *Real Python – How to Import Functions from Another File*

---

## Program 2 – Circle Area and Circumference (`nazario5_2.py`)

### Description
A program that calculates and displays both the area and circumference of a circle.  
Demonstrates use of the `math` module and the creation of value-returning and void functions.

### Features
- Imports the `math` library to access `pi`.
- Prompts for a circle’s radius and passes it to two separate functions:
  - `a(radius)` returns the circle’s area.
  - `circum(radius)` prints the circumference directly.
- Uses formatted output with precision up to four decimal places.

### Files
- `nazario5_2.py` — complete implementation of the area and circumference functions:contentReference[oaicite:2]{index=2}.

### Notes
- Reinforces modular function design and arithmetic operations with library imports.
- Demonstrates parameter passing, return values, and formatted output.
- References:  
  - *Python 3 Documentation – math Module*  
  - *Python for Beginners – Functions and Arguments*

---

## Program 3 – Circle Module Import (`nazario5_3.py`)

### Description
A Python script that imports the `nazario5_2` module and reuses its functions to calculate and display circle properties.  
Demonstrates modular reuse and namespace qualification.

### Features
- Imports `nazario5_2` as `n`.
- Requests user input for the radius.
- Calls the `a()` and `circum()` functions from the imported module.
- Displays formatted results consistent with the previous program.

### Files
- `nazario5_3.py` — complete implementation reusing imported functions:contentReference[oaicite:3]{index=3}.

### Notes
- Demonstrates modular reuse and proper function referencing.
- Reinforces encapsulation and modular design across separate files.
- References:  
  - *Python 3 Documentation – import Statement*  
  - *Real Python – Organizing Code with Modules*

---

## How to Run

### Requirements
- Python 3.8 or newer

### Execution
Run each program separately from the command line:
```bash
python nazario5_1.py
python nazario5_2.py
python nazario5_3.py
