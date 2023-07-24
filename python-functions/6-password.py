def validate_password(password):
    # Check length
    if len(password) < 8:
        return False

    # Check for at least one uppercase letter, one lowercase letter, and one digit
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

        if has_uppercase and has_lowercase and has_digit:
            break

    # Check for spaces
    if ' ' in password:
        return False

    return has_uppercase and has_lowercase and has_digit
