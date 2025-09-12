from werkzeug.security import safe_str_cmp

def compare_strings(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False  # Early exit if lengths do not match
    return safe_str_cmp(a, b)
