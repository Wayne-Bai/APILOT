from werkzeug.exceptions import BadRequest

def quote_header_value(header_value):
    if not isinstance(header_value, str):
        raise BadRequest("Header value must be a string.")
    
    # Quote the header value if it contains special characters
    if any(char in header_value for char in [' ', ',', '"', '\\']):
        return f'"{header_value}"'
    
    return header_value
