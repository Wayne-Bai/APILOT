from werkzeug.http import unquote_header_value

# Sample header value to demonstrate unquoting
header_value = 'hello%20world%21'

# Unquote the header value
unquoted_value = unquote_header_value(header_value)
print("Unquoted header value:", unquoted_value)
