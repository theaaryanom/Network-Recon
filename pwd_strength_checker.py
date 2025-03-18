#!/usr/bin/env python3
import re

def check_password_strength(password):
    # Define criteria for password strength
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search("[a-z]", password) is not None
    uppercase_criteria = re.search("[A-Z]", password) is not None
    digit_criteria = re.search("[0-9]", password) is not None
    special_char_criteria = re.search("[!@#$%^&*()_+{}\[\]:;<>,.?/~`-]", password) is not None

    # Calculate the strength score
    strength_score = 0
    if length_criteria:
        strength_score += 1
    if lowercase_criteria:
        strength_score += 1
    if uppercase_criteria:
        strength_score += 1
    if digit_criteria:
        strength_score += 1
    if special_char_criteria:
        strength_score += 1

    # Determine the strength level
    if strength_score == 5:
        return "Strong: Password meets all requirements."
    elif strength_score >= 3:
        return "Moderate: Password meets most requirements."
    else:
        return "Weak: Password does not meet minimum requirements."

def get_password():
    # Get password input from the user
    return input("Enter your password: ")

def display_strength_result(password):
    # Display the password strength result
    result = check_password_strength(password)
    print("\nPassword Strength Analysis:")
    print("--------------------------")
    print(f"Password: {password}")
    print(f"Strength: {result}")

if __name__ == "__main__":
    print("Password Strength Checker")
    print("------------------------")
    password = get_password()
    display_strength_result(password)
