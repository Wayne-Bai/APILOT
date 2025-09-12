from werkzeug.security import compare_strings
# Example usage
str1 = "hello"
str2 = "world"
result = compare_strings(str1, str2)
print(result)  # Output: True
