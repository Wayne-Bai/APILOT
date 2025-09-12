from werkzeug.http import dump_header

def dump_http_header(header_name, header_value):
    """Dump an HTTP header."""
    return dump_header(header_name, header_value)

# Example usage:
header_name = "Content-Type"
header_value = "application/json; charset=utf-8"
result = dump_http_header(header_name, header_value)

print(result)
