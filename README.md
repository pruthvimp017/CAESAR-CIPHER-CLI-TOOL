# Caesar Cipher CLI Tool (Windows)

## Overview

This project implements a **Command Line Interface (CLI)** based Caesar Cipher encryption and decryption tool for Windows systems.  
The tool allows users to encrypt or decrypt text using a fixed shift value supplied through command-line arguments.

The Caesar Cipher is a classical substitution cipher and is used in this project strictly for **educational and demonstrative purposes**.

---

## Features

- Encrypt and decrypt text using the Caesar Cipher  
- Accepts input through command-line arguments  
- Preserves uppercase, lowercase, numbers, and special characters  
- Supports large shift values using modulo arithmetic  
- Compatible with Windows Command Prompt and PowerShell  
- Scriptable and automation-friendly  

---

## Technologies Used

- **Programming Language:** Python 3  
- **Platform:** Windows  
- **Library:** argparse (Python standard library)  

---

## Requirements

- Windows Operating System  
- Python 3.8 or higher  
- Python added to system PATH  



## Usage
```
### Encrypt Text

python caesar.py -t "Hello World!" -s 3
Khoor Zruog!

### Decrypt Text

python caesar.py -t "Khoor Zruog!" -s 3 -d
Hello World!

### Help Menu
python caesar.py --help

| Option            | Description             |
| ----------------- | ----------------------- |
| `-t`, `--text`    | Input text              |
| `-s`, `--shift`   | Shift value (integer)   |
| `-d`, `--decrypt` | Enables decryption mode |
