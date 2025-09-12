from werkzeug.security import safe_str_cmp

def constant_time_compare(str1, str2):
    # Compare two strings in constant time
    return safe_str_cmp(str1, str2)

# Example usage
str1 = "secret_value"
str2 = "user_input_value"
result = constant_time_compare(str1, str2)
print("Strings are equal:" if result else "Strings are not equal.")
