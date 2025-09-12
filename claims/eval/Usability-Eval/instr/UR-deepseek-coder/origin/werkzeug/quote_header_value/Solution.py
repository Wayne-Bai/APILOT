from werkzeug.http import quote_header_value

def quote_header(value):
    return quote_header_value(value)

# Example usage
header_value = "Example Header Value"
quoted_value = quote_header(header_value)
print(quoted_value)
