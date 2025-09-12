from werkzeug.http import quote_header_value

def safe_quote_header_value(value):
    """
    Quote a header value if necessary.
    
    Parameters:
    value (str): The header value to be quoted.
    
    Returns:
    str: A quoted header value if necessary, otherwise the original value.
    """
    return quote_header_value(value)

# Example usage
header_value = 'This is a test value with special chars: ; , / ?'
quoted_value = safe_quote_header_value(header_value)
print(quoted_value)
