from werkzeug.http import unquote_header

def unquote_header_value(header):
    """
    Unquotes a header value.
    
    :param header: The header value to be unquoted.
    :return: The unquoted header value.
    """
    return unquote_header(header)

# Example usage:
header = "Hi%20World"
unquoted_header = unquote_header_value(header)
print(unquoted_header)  # Output: Hi World
