from werkzeug.security import safe_compare_digest

def constant_time_compare(known_string, user_string):
    """
    Compare two strings in constant time.

    :param known_string: The string of known length to compare against.
    :param user_string: The user-provided string.
    :return: True if the strings are equal, otherwise False.
    """
    return safe_compare_digest(known_string, user_string)

# Example usage:
known_string = "known_secret"
user_string = "user_input"

if constant_time_compare(known_string, user_string):
    print("Strings are equal.")
else:
    print("Strings are not equal.")
