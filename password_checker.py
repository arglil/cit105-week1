import re
from typing import List, Tuple


def get_missing_password_requirements(password: str) -> List[str]:
    """Return a list of missing password requirements."""
    if not isinstance(password, str):
        raise TypeError("Password must be a string.")

    missing = []

    if len(password) < 8:
        missing.append("at least 8 characters")
    if not re.search(r"[A-Z]", password):
        missing.append("an uppercase letter")
    if not re.search(r"[a-z]", password):
        missing.append("a lowercase letter")
    if not re.search(r"\d", password):
        missing.append("a number")
    if not re.search(r"[^A-Za-z0-9]", password):
        missing.append("a special character")

    return missing


def is_strong_password(password: str) -> bool:
    """Return True only if the password meets all strength requirements."""
    return not get_missing_password_requirements(password)


def check_password_strength(password: str) -> Tuple[bool, List[str]]:
    """Return (is_strong, missing_requirements)."""
    missing = get_missing_password_requirements(password)
    return (not missing), missing


def password_strength(password: str) -> Tuple[bool, List[str]]:
    """Alias for check_password_strength for compatibility."""
    return check_password_strength(password)


def describe_password_strength(password: str) -> str:
    """Return a human-friendly explanation of password strength."""
    is_strong, missing = check_password_strength(password)

    if is_strong:
        return "Strong password. It meets all requirements."

    if len(missing) == 1:
        return f"Password is missing: {missing[0]}."

    return "Password is missing: " + ", ".join(missing[:-1]) + ", and " + missing[-1] + "."


if __name__ == "__main__":
    user_input = input("Enter a password: ")
    print(describe_password_strength(user_input))
