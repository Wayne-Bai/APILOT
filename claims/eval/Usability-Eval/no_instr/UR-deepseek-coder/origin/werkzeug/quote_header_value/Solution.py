from werkzeug.http import quote_header_value

def quote_header_value_if_necessary(value):
    return quote_header_value(value)

# Example usage
header_value = "Example Header Value"
quoted_value = quote_header_value_if_necessary(header_value)
print(quoted_value)
