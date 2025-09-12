from werkzeug.http import quote_header_value

def quote_if_necessary(header_value):
    # Use Werkzeug's quote_header_value to quote the header value if necessary
    quoted_value = quote_header_value(header_value)
    return quoted_value

# Example usage
header_value = 'text/plain; charset="utf-8"'
quoted_value = quote_if_necessary(header_value)
print(f'Quoted Header Value: {quoted_value}')
