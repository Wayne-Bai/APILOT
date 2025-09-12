def constant_time_compare(val1, val2):
    return val1 == val2

# Example usage:
val1 = "known_string"
val2 = "known_string"

if constant_time_compare(val1, val2):
    print("Strings are equal.")
else:
    print("Strings are not equal.")
