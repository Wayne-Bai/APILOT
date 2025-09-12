from werkzeug.security import safe_str_cmp

def compare_strings(known_string: str, unknown_string: str) -> bool:
    """
    Function to compare two strings.

    Parameters:
    - known_string (str): The string whose length is known in advance.
    - unknown_string (str): The string whose content should be compared to known_string.

    Returns:
    - bool: True if the strings match, False otherwise.
    """

    # Check if both strings are not empty and have known length
    if known_string and unknown_string and len(known_string) > 0 and len(unknown_string) > 0:
        # Use safe_str_cmp for constant time string comparison
        return safe_str_cmp(known_string, unknown_string)
    else:
        return False

# Test the function
known_str = "hello world"
unknown_str = "hello world"
print(compare_strings(known_str, unknown_str))  # Output: True

unknown_str = "hello Python"
print(compare_strings(known_str, unknown_str))  # Output: False
