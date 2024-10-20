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

import re

def check_password_strength(password):
    # Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_character_criteria = re.search(r'[@$!%*?&]', password) is not None

    # Calculate strength
    strength_score = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        number_criteria,
        special_character_criteria
    ])

    # Determine strength level
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    elif strength_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Provide feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should contain at least one number.")
    if not special_character_criteria:
        feedback.append("Password should contain at least one special character (e.g., @$!%*?&).")

    return strength, feedback

# Example usage
if __name__ == "__main__":
    password = input("Enter your password: ")
    strength, feedback = check_password_strength(password)
    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for line in feedback:
            print(f"- {line}")

# Print the end of the program
end = """
Thank you for using the Password Complexity Checker!
"""
end_colored = colored(end, color="cyan")
print(end_colored)

# End of the program
