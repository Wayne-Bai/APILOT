from werkzeug.http import unquote_header_value

def unquote_header(value):
    return unquote_header_value(value)

# Example usage
header_value = 'application/json;charset=utf-8'
unquoted_value = unquote_header(header_value)
print(unquoted_value)  # Output: application/json;charset=utf-8
