import string
import random

def calculate_password_strength(password):
    # Define character types
    has_lowercase = any(c.islower() for c in password)
    has_uppercase = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    # Calculate password length score
    length_score = min(1.0, len(password) / 12)  # Assuming a desirable length of 12
    
    # Calculate character types score
    char_types_score = (has_lowercase + has_uppercase + has_digit + has_special) / 4.0
    
    # Calculate randomness score
    randomness_score = random.uniform(0.5, 1.0)  # Simplified randomness score
    
    # Calculate overall strength score (adjust weights as needed)
    strength_score = (length_score + char_types_score + randomness_score) / 3.0
    
    return strength_score

def interpret_strength_score(score):
    if score >= 0.9:
        return "Very Strong"
    elif score >= 0.7:
        return "Strong"
    elif score >= 0.5:
        return "Moderate"
    elif score >= 0.3:
        return "Weak"
    else:
        return "Very Weak"

# Input password to be checked
password = input("Enter a password: ")

# Calculate and interpret the password strength
strength_score = calculate_password_strength(password)
strength_indicator = interpret_strength_score(strength_score)

print(f"Password Strength: {strength_indicator}")
