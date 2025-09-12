from werkzeug.security import safe_str_compare

def constant_time_compare(s1: str, s2: str) -> bool:
    return safe_str_compare(s1, s2)
