## PDF-to-Text Extractor

A simple Python utility to extract all text from a PDF file into a single plain‑text file.  
Uses `pypdf` for PDF parsing and Tkinter for a file‑selection GUI.

---

### Table of Contents
1. [Features](#features)  
2. [Requirements](#requirements)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Project Structure](#project-structure)  
6. [Configuration](#configuration)  
7. [Contributing](#contributing)  
8. [License](#license)  

---

## Features
- **One‑click PDF selection** via a simple Tkinter dialog.  
- **Full‑document text extraction** into one consolidated `.txt` file.  
- **Metadata‑aware output naming** with safe fallback to the PDF filename.  
- **UTF‑8 encoding** to preserve special characters.  
- **Organized output directory** (`output/`) auto‑created if needed.

---

## Requirements
- **Python 3.8+**  
- **pypdf** (for reading and parsing PDF files)  
- **Tkinter** (for the file‑selection dialog)  

Install via pip:
```bash
pip install pypdf
