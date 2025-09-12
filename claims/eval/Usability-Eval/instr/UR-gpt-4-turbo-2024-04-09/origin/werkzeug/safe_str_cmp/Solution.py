import os
from hmac import compare_digest

def secure_string_compare(val1, val2):
    return compare_digest(val1, val2)

# Example usage
string1 = "secure_string"
string2 = "secure_string"
result = secure_string_compare(string1, string2)
print("Strings are equal:" , result)
