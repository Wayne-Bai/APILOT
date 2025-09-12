from werkzeug.http import parse_options_header

def unquote_header_value(header_value):
    """
    Unquotes a header value using Werkzeug.
    
    Parameters:
    - header_value (str): The header value to unquote.

    Returns:
    - str: The unquoted header value.
    """
    value, options = parse_options_header(header_value)
    return value

# Example usage
quoted_header_value = '"application/json; charset=utf-8"'
unquoted_value = unquote_header_value(quoted_header_value)
print("Unquoted value:", unquoted_value)
