from werkzeug import safe_str_cmp

# Function to compare two strings in constant time
def constant_string_compare(str1, str2, len1):
    if len1 != len(str2):
        raise ValueError("Second string length must be equal to the first string length")

    hash1 = 0
    for i in range(len1):
        hash1 ^= ord(str1[i]) << (8 * (i % 4))

    hash2 = 0
    for i in range(len1):
        hash2 ^= ord(str2[i]) << (8 * (i % 4))

    return safe_str_cmp(str1[:len1], str2[:len1])

# Example usage
str1 = "constantstring"
str2 = "constantstring"

# Assume len1 to be the length of str1
len1 = len(str1)

print(constant_string_compare(str1, str2, len1))
