import re


def check_password(password):
    """
    Analyze a password and return:
    - score (0-100)
    - strength level
    - feedback
    """

    score = 0
    feedback = []

    # -------------------------
    # 1. Password Length
    # -------------------------

    length = len(password)

    if length >= 16:
        score += 30
    elif length >= 12:
        score += 25
    elif length >= 10:
        score += 20
    elif length >= 8:
        score += 10
    else:
        feedback.append("Use at least 8 characters.")

    # -------------------------
    # 2. Character Variety
    # -------------------------

    has_uppercase = bool(re.search(r"[A-Z]", password))
    has_lowercase = bool(re.search(r"[a-z]", password))
    has_number = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[^A-Za-z0-9]", password))

    if has_uppercase:
        score += 15
    else:
        feedback.append("Add an uppercase letter.")

    if has_lowercase:
        score += 15
    else:
        feedback.append("Add a lowercase letter.")

    if has_number:
        score += 15
    else:
        feedback.append("Add a number.")

    if has_special:
        score += 15
    else:
        feedback.append("Add a special character.")

    # -------------------------
    # 3. Repeated Characters
    # -------------------------

    if re.search(r"(.)\1\1", password):
        score -= 10
        feedback.append(
            "Avoid repeating the same character multiple times."
        )

    # -------------------------
    # 4. Sequential Characters
    # -------------------------

    sequences = [
        "123456789",
        "abcdefghijklmnopqrstuvwxyz",
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm"
    ]

    password_lower = password.lower()

    for sequence in sequences:
        for i in range(len(sequence) - 2):
            if sequence[i:i + 3] in password_lower:
                score -= 10
                feedback.append(
                    "Avoid predictable sequences like abc or 123."
                )
                break
        else:
            continue
        break

    # -------------------------
    # 5. Common Passwords
    # -------------------------

    common_passwords = {
        "password",
        "123456",
        "12345678",
        "123456789",
        "qwerty",
        "password123",
        "admin",
        "letmein",
        "welcome",
        "iloveyou",
        "monkey",
        "dragon"
    }

    if password_lower in common_passwords:
        score = min(score, 10)
        feedback.append(
            "This is a commonly used password."
        )

    # -------------------------
    # 6. Prevent Negative Scores
    # -------------------------

    score = max(0, min(score, 100))

    # -------------------------
    # 7. Determine Strength
    # -------------------------

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
    print("=" * 45)
    print("        🔐 PASSWORD STRENGTH CHECKER")
    print("=" * 45)

    password = input("\nEnter a password to check: ")

    score, strength, feedback = check_password(password)

    print("\n" + "-" * 45)
    print("RESULTS")
    print("-" * 45)

    print(f"Score:    {score}/100")
    print(f"Strength: {strength}")

    if feedback:
        print("\nSuggestions:")

        for suggestion in feedback:
            print(f"  • {suggestion}")
    else:
        print("\n✓ No basic improvements detected!")

    print("\nYour password was checked locally.")
    print("It was not saved or transmitted.")


if __name__ == "__main__":
    main()
