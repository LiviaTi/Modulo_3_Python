import string

def valid_size(password: str) -> bool:
    return 8 <= len(password) <= 16

def has_upper(password: str) -> bool:
    return any(char.isupper() for char in password)

def has_lower(password: str) -> bool:
    return any(char.islower() for char in password)

def has_digit(password: str) -> bool:
    return any(char.isdigit() for char in password)

def has_especial_char(password: str) -> bool:
    return any(char in string.punctuation for char in password)

def is_clean_spaces(password: str) -> bool:
    if any(char.isspace() for char in password):
        return False
    return True

def is_valid_password(password: str) -> bool:
    checks = [
        valid_size,
        has_upper,
        has_lower,
        has_digit,
        has_especial_char,
        is_clean_spaces,
    ]
    return all(check(password) for check in checks)