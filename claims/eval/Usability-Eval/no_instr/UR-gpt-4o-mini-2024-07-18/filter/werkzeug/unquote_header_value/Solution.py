from werkzeug.http import unquote

def unquote_header_value(header_value):
    return unquote(header_value)

# Example usage
header_value = 'Hello%20World%21'
unquoted_value = unquote_header_value(header_value)
print(unquoted_value)  # Output: Hello World!
