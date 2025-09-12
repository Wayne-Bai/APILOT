import werkzeug.security

def constant_time_compare(string1, string2):
    return werkzeug.security.safe_str_cmp(string1, string2)
