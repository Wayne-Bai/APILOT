from werkzeug.security import safe_str_cmp

def compare_strings(s1, s2, known_length):
    if len(s1) == known_length:
        return safe_str_cmp(s1, s2) == 0
    elif len(s2) == known_length:
        return safe_str_cmp(s2, s1) == 0
    else:
        raise ValueError("At least one string length must be known in advance.")
