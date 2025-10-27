# elevate_project_1

📘 Project Overview



This Python project analyzes the strength of passwords and generates custom wordlists based on user-provided data. It demonstrates password security awareness and provides practical insight into how personal information can be leveraged in password attacks — for ethical cybersecurity research only.

⚙️ Features
Password Strength Analyzer: Calculates entropy and rates password strength as Very Weak, Weak, Moderate, Strong, or Very Strong.
Custom Wordlist Generator: Builds personalized password lists using details like names, pets, and dates.
Leetspeak Variants: Converts characters (e.g., a → @, s → 5, o → 0) for realistic combinations.
Export Functionality: Saves generated wordlists to .txt files for use with password-testing tools.
No External Libraries: Fully functional without installing extra packages.
🧰 Tools Used
Language: Python 3
Modules: re, math, argparse, datetime (all built-in)
IDE: Visual Studio Code
🚀 How to Run
Save the script as pwtool_simple.py in your project folder.
Open VS Code Terminal and navigate to the folder containing the script.
Run the following command:
python pwtool_simple.py --name "aditya" --pet "milo" --dates "2003,1999" --testpass "P@ssw0rd123"

The tool will:
Display the password strength analysis in the terminal.
Generate a wordlist.txt file in the same folder.
🧪 Example Output
Password Analysis:
  Entropy: 65.42 bits
  Strength: Strong

Generating wordlist from 2 base words, years={'2003', '1999'}
Saved 5000 words → wordlist.txt
