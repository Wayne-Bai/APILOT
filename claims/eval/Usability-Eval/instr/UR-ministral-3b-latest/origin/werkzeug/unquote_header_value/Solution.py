from werkzeug.wrappers import Request as werkzeug_Request

def unquote_header(header):
    """
    Unquotes a header value.
    """
    return werkzeug_Request.unquote(header)

# Example usage
header_value = "X-Test%20Header: value"
unquoted_header = unquote_header(header_value)
print(unquoted_header)
