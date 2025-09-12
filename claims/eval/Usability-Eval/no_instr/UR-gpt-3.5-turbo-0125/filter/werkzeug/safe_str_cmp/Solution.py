
# Import required libraries
from werkzeug.security import safe_str_cmp

# Compare strings in constant time
def compare_strings(str1, str2):
    return safe_str_cmp(str1, str2)

# Example usage
str1 = "hello"
str2 = "world"
result = compare_strings(str1, str2)
print(result)
