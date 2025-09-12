from werkzeug.utils import secure_filename

def compare_strings_constant_time(str1, str2, known_length):
    """
    Compare two strings in constant time.
    
    :param str1: The first string to compare.
    :param str2: The second string to compare.
    :param known_length: The known length of at least one of the strings.
    :return: True if the strings are equal, False otherwise.
    """
    if len(str1) != known_length or len(str2) != known_length:
        return False
    
    result = 0
    for x, y in zip(str1, str2):
        result |= ord(x) ^ ord(y)
    
    return result == 0

# Example usage:
str1 = "example"
str2 = "example"
known_length = len(str1)

print(compare_strings_constant_time(str1, str2, known_length))  # Output: True
