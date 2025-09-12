from werkzeug.datastructures import Headers

def unquote_header(header):
    """
    Unquotes a header value.

    Args:
        header (str): The header value to unquote.

    Returns:
        str: The unquoted header value.
    """
    headers = Headers()
    return headers.parse_list_header(header)[0]

# Example usage:
header = '#######"Spanish"'  # The header value to unquote
unquoted_header = unquote_header(header)
print(unquoted_header)
