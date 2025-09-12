
from werkzeug import secure_compare

def compare_strings(str1, str2):
    # Ensure that at least one of the strings has a known length
    if len(str1) == 0 or len(str2) == 0:
        raise ValueError("Cannot compare empty strings")
    
    # Use secure_compare to compare the strings
    return secure_compare(str1, str2)
