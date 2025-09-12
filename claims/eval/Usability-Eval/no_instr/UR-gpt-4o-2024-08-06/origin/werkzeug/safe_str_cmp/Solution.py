from werkzeug.security import safe_str_cmp

# Example of comparing two strings in a somewhat constant time manner
def compare_strings(str1, str2):
    return safe_str_cmp(str1, str2)

# Usage
result = compare_strings("securepassword", "securepassword")
print("Strings match:", result)
