from werkzeug.security import safe_str_cmp

def compare_strings(str1, str2):
    # Assume the length of str1 is known in advance
    length_of_str1 = len(str1)
    
    if length_of_str1 != len(str2):
        return False
    
    return safe_str_cmp(str1, str2)

# Example usage
result = compare_strings("hello", "hello")
print(result)  # Output: True

result = compare_strings("hello", "world")
print(result)  # Output: False
