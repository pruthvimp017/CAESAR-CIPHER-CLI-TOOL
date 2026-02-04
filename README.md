Caesar Cipher CLI Tool (Windows)
Overview

This project implements a Command Line Interface (CLI) based Caesar Cipher encryption and decryption tool for Windows systems.
The tool allows users to encrypt or decrypt text using a fixed shift value supplied through command-line arguments.

The Caesar Cipher is a classical substitution cipher and is used in this project strictly for educational and demonstrative purposes.

Features

Encrypt and decrypt text using the Caesar Cipher

Accepts input through command-line arguments

Preserves uppercase, lowercase, numbers, and special characters

Supports large shift values using modulo arithmetic

Compatible with Windows Command Prompt and PowerShell

Scriptable and automation-friendly

Technologies Used

Programming Language: Python 3

Platform: Windows

Library: argparse (Python standard library)

Requirements

Windows Operating System

Python 3.8 or higher

Python added to system PATH

Verify Python Installation
python --version

Usage
Encrypt Text
python caesar.py -t "Hello World!" -s 3


Output

Khoor Zruog!

Decrypt Text
python caesar.py -t "Khoor Zruog!" -s 3 -d


Output

Hello World!

Help Menu
python caesar.py --help

Command-Line Arguments
Option	Description
-t, --text	Input text
-s, --shift	Shift value (integer)
-d, --decrypt	Enables decryption mode
Flowchart Diagram

Figure: Flowchart representing the working of the Caesar Cipher CLI tool for encryption and decryption.

Applications

Learning basic cryptography concepts

Understanding command-line based programs

Academic assignments and lab submissions

Foundation for advanced encryption techniques

Limitations

Not suitable for real-world secure communication

Vulnerable to brute-force attacks

Intended only for educational use

Conclusion

This project demonstrates a clean and functional implementation of the Caesar Cipher using a Windows-based CLI approach. While the cipher itself is not secure for modern applications, the project effectively illustrates encryption logic, character manipulation, and command-line program design.
