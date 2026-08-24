import re


def check_password(password):
    """
    Checks the strength of a password.

    Returns:
        score: A number from 0-100
        strength: Strength rating
        feedback: List of suggestions
    """

    score = 0
    feedback = []

    # Length
    length = len(password)

    if length >= 16:
        score += 30
    elif length >= 12:
        score += 25
    elif length >= 8:
        score += 15
    else:
        feedback.append("Use at least 8 characters.")

    # Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase letters
    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Add at least one lowercase letter.")

    # Numbers
    if re.search(r"\d", password):
        score += 15
    else:
        feedback.append("Add at least one number.")

    # Special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 15
    else:
        feedback.append("Add a special character such as !, @, #, or $.")

    # Penalize obvious repeated characters
    if re.search(r"(.)\1\1", password):
        score -= 10
        feedback.append("Avoid repeating the same character multiple times.")

    # Penalize common passwords
    common_passwords = {
        "password",
        "123456",
        "12345678",
        "qwerty",
        "password123",
        "admin",
        "letmein",
        "welcome"
    }

    if password.lower() in common_passwords:
        score = min(score, 20)
        feedback.append("Avoid common passwords.")

    # Keep score between 0 and 100
    score = max(0, min(score, 100))

    # Determine strength
    if score < 30:
        strength = "Very Weak"
    elif score < 50:
        strength = "Weak"
    elif score < 70:
        strength = "Moderate"
    elif score < 90:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return score, strength, feedback


def main():
    print("=" * 40)
    print("       PASSWORD STRENGTH CHECKER")
    print("=" * 40)

    password = input("Enter a password to check: ")

    score, strength, feedback = check_password(password)

    print("\nResults")
    print("-" * 40)
    print(f"Score:    {score}/100")
    print(f"Strength: {strength}")

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("\nGreat! No basic improvements were detected.")

    print("\nYour password was only checked locally.")
    print("It is not saved or transmitted.")


if __name__ == "__main__":
    main()
