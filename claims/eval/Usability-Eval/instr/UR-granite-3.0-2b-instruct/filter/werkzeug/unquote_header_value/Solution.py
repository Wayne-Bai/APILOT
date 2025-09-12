from werkzeug import Headers

def unquote_header(header_value):
    return Headers().get(header_value).value

# Example usage:
header_value = "Header%20Value"
unquoted_value = unquote_header(header_value)
print(unquoted_value)  # Output: Header Value
