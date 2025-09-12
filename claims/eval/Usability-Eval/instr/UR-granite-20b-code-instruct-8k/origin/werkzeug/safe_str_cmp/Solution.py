
from werkzeug.security import check_password_hash

def compare_strings(string1, string2):
    return check_password_hash(string1, string2)
