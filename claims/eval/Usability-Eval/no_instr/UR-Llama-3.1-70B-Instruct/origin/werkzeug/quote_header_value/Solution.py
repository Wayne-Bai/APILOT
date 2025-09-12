from werkzeug.datastructures import MIMEAccept
from email.utils import quote

def quote_header_value(header_value):
    """
    Quotes the header value if necessary.
    
    Args:
    header_value (str): The header value to be quoted.
    
    Returns:
    str: The quoted header value if necessary, otherwise the original value.
    """
    # Using MIMEAccept to determine if the header value needs to be quoted
    if MIMEAccept.mimetype_is_xxx_unquoted(header_value):
        return quote(header_value)
    return header_value

# Example usage:
header_value = "Hello, World!"
quoted_value = quote_header_value(header_value)
print(quoted_value)
