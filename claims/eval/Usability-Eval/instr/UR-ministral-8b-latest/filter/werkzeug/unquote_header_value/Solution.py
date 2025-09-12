from werkzeug import unquote

# Sample header value
header_value = 'Hello%20World'

# Unquoting the header value
unquoted_value = unquote(header_value)

print(unquoted_value)  # Output: Hello World
