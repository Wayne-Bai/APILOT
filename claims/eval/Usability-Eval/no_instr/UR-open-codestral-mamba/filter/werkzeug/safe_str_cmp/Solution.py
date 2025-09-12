from werkzeug.security import safe_str_cmp

def compare_strings(str1, str2):
    # Check if lengths of strings are equal
    if len(str1) != len(str2):
        return False
    else:
        return safe_str_cmp(str1, str2)

# Test the function
str1 = "Hello, world!"
str2 = "Hello, world!"
print(compare_strings(str1, str2))  # Output: True

str3 = "Hello, world!"
str4 = "Hello, Werner!"
print(compare_strings(str3, str4))  # Output: False
