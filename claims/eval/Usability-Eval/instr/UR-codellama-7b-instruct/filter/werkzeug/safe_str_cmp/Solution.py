
from werkzeug.utils import compare_strings

# Compare two strings in constant time, assuming the length of at least one string is known in advance
compare_result = compare_strings(string1, string2)
