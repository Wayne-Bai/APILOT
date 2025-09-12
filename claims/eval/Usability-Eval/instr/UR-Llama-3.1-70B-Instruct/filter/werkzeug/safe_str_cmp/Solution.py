from werkzeug import security
import hmac
import time

def compare_strings_known_length(a, b, b_known_length):
    """
    Compare strings in somewhat constant time.
    
    This function requires that the length of at least one string is known in advance.
    It fulfills the purpose by using the hmac.compare_digest function.
    
    Parameters:
    a (str): The string with unknown length.
    b (str): The string with known length.
    b_known_length (int): The known length of string b.
    
    Returns:
    bool: Whether the strings are equal or not.
    """
    if len(b)!= b_known_length:
        raise ValueError("The known length of string b does not match its actual length")
    
    return hmac.compare_digest(a, b)


def compare_strings_constant_time(a, b):
    """
    Compare strings in constant time.
    
    This function does not require any known lengths of the strings.
    However, it's less efficient than compare_strings_known_length.
    
    Parameters:
    a (str): The first string to compare.
    b (str): The second string to compare.
    
    Returns:
    bool: Whether the strings are equal or not.
    """
    return hmac.compare_digest(a, b)


# Example usage
if __name__ == "__main__":
    a = "Hello, World!"
    b = "Hello, World!"
    
    start_time = time.time()
    result_known_length = compare_strings_known_length(a, b, len(b))
    end_time = time.time()
    print(f"Strings are equal: {result_known_length}")
    print(f"Time taken (known length): {end_time - start_time} seconds")
    
    start_time = time.time()
    result_constant_time = compare_strings_constant_time(a, b)
    end_time = time.time()
    print(f"Strings are equal: {result_constant_time}")
    print(f"Time taken (constant time): {end_time - start_time} seconds")
