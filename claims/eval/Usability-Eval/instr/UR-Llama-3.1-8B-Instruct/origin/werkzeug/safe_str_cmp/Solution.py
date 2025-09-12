from werkzeug.security import _hmac_compare_digest

def compare_strings(string1, string2, known_length1, known_length2):
    # Check if the lengths of the strings match
    if len(string1)!= known_length1 or len(string2)!= known_length2:
        return False

    # Compare the strings in constant time using a slow comparison
    return _hmac_compare_digest(string1.encode('utf-8'), string2.encode('utf-8'))
