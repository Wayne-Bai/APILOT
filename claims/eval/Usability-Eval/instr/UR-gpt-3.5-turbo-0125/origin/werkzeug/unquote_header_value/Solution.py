
from werkzeug.http import parse_options_header

def unquote_header_value(header_value):
    return parse_options_header(header_value)[0]

# Example Usage:
header_value = 'attachment; filename="example.txt"'
unquoted_value = unquote_header_value(header_value)
print(unquoted_value)
