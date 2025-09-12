from werkzeug.http import quote_header_value

def quote_value_if_necessary(value):
    """
    Quotes a header value if necessary to ensure it is valid.

    :param value: The header value to be quoted if needed.
    :return: The quoted header value.
    """
    return quote_header_value(value)

# Example usage:
header_value = 'This is an example header "value" with special chars'
quoted_value = quote_value_if_necessary(header_value)
print("Quoted Header Value:", quoted_value)
