# IB-to-US-GPA Converter
A Python command-line tool that converts IB scores (0-45) to an approximate US 4.0 GPA scale using linear interpolation.

## Features
- **Modular Design:** Uses dedicated functions for input collection, core bonus calculation, and GPA conversion.
- **Input Validation:** Built-in error handling prevents crashes from typos or out-of-range grades.
- **Core Bonus Integration:** Automatically adds EE/TOK bonus points (0-3) to individual subject totals (6-7).

## How to Run
1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Run the the script in your terminal:
   ```bash
   python3 ib_gpa_converter.py
