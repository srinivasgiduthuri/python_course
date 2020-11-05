def has_upper(val):
    for char in str(val):
        if char.isupper():
            return True
    else:
        return False


def has_digit(val):
    for char in str(val):
        if char.isnumeric():
            return True
    else:
        return False


def extract_upper_chars(val):
    upper_chars = []
    for char in str(val):
        if char.isupper():
            upper_chars.append(char)
    return "".join(upper_chars)
