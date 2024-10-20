## PRODIGY_CS_03

# Password Complexity Checker

## Overview
The **Password Complexity Checker** program evaluates the strength of a password based on specific criteria. It helps users understand the complexity of their passwords and provides feedback on how to improve them.

## Features
- Checks if the password meets the following criteria:
  - At least 8 characters long
  - Contains both uppercase and lowercase characters
  - Contains at least one digit
  - Contains at least one special character (e.g., @$!%*?&)
- Provides a strength rating for the password:
  - Very Strong
  - Strong
  - Moderate
  - Weak
  - Very Weak
- Offers feedback on what aspects of the password need improvement.

## Requirements
- Python 3.x
- Termcolor
- Regular Expressions (re module)

## Installation
1. **Install Python**: Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. **Install Required Libraries**: Use pip to install the necessary libraries:
   ```bash
   pip install termcolor
   ````
# Usage
To run the Password Complexity Checker program, execute the following command in your terminal or command prompt:

bash
python password_complexity_checker.py

# Instructions
Enter a password when prompted.
The program will evaluate the password and display its strength along with feedback on how to improve it.
Example Command
bash
Enter your password: MyP@ssw0rd!
Password Strength: Very Strong

# Code Explanation
The program consists of the following key components:

Title Display: The title "Password Complexity Checker" is printed in a stylized ASCII format using the pyfiglet library, with blended colors for visual appeal.
Creator Information: Displays the creator's name and social media handles.
Description: Outlines the purpose of the program and the criteria for password strength.
Instructions: Provides guidance for users on how to use the program.
Password Strength Check:
check_password_strength(password): This function evaluates the password against the defined criteria and returns the strength rating and feedback.
User Interaction: Prompts the user to input a password and displays the strength and feedback.

# Creator
Created by: Dem0saic
GitHub: dem0saic
LinkedIn: owusuvincent

# License
This project is licensed under the MIT License - see the LICENSE file for details.
