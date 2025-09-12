from werkzeug.http import unquote_header_value

def unquote_header_value(value):
    # Unquote a header value (RFC 2616) if needed
    return value[1:-1] if value.startswith('"') and value.endswith('"') else value

# Test the function
print(unquote_header_value('"test"'))
print(unquote_header_value('test'))
