from werkzeug.security import safe_str_cmp

# Define the two strings to be compared
string1 = "hello"
string2 = "world"

# Use the safe_str_cmp() function to compare the strings
if safe_str_cmp(string1, string2):
    print("The two strings are equal")
else:
    print("The two strings are not equal")
