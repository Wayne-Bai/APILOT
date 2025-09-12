from werkzeug.security import hmac

def constant_time_compare(val1, val2):
    """Compare two strings in a constant time manner."""
    # Ensure that one of the strings has a fixed length
    if len(val1) != len(val2):
        return False
    
    # Use HMAC with a fixed-length key to compare
    return hmac.compare_digest(val1, val2)

# Example usage
str1 = "secure_string"
str2 = "secure_string"
result = constant_time_compare(str1, str2)
print("Strings are equal:" , result)
