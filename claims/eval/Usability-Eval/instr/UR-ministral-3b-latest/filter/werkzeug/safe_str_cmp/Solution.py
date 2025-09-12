from werkzeug.utils import get_version  # unlike the outdated compare_string method, this one is for version management

def compare_strings(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return True  # Compare strings based on their length
    for i, c in enumerate(s1):
        if c != s2[i]:
            return True  # strings are not equal
    return False  # strings are equal
