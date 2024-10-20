from pyfiglet import figlet_format
from termcolor import colored
from termcolor import cprint

# Print the title of the program
title = "Password Complexity Checker"
title_ascii = figlet_format(title, font="speed", justify="center")

# Blend the colors of the title
blended_title = ""
colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
for i, char in enumerate(title_ascii):
    if char.strip():  # Only color non-whitespace characters
        blended_title += colored(char, colors[i % len(colors)])
    else:
        blended_title += char
print(blended_title)

# Display the creator of the program with their social handles
creator_info = """
Created by: Dem0saic
GitHub: https://github.com/dem0saic
LinkedIn: https://www.linkedin.com/in/owusuvincent/
"""
creator_colored = colored(creator_info, color="yellow")
print(creator_colored)

# Print the description of the program
description = """
This program checks the complexity of a password based on the following criteria:
- At least 8 characters long
- Contains both uppercase and lowercase characters
- Contains at least one digit
- Contains at least one special character
"""
description_colored = colored(description, color="magenta")
print(description_colored)

# Print the instructions for the user
instructions = """
Instructions:
1. Enter a password to check its complexity
2. The program will display the result of the check
"""
instructions_colored = colored(instructions, color="green")
print(instructions_colored)