from werkzeug.http import quote_header_value

def quote_header(header_value):
    """
    Quote a header value if necessary.

    :param header_value: The value of the header.
    :return: The quoted header value if necessary.
    """
    return quote_header_value(header_value)

# Example usage:
header_value = "filename.txt"
quoted_header_value = quote_header(header_value)
print(quoted_header_value)

# Another example with special characters:
header_value_with_special_chars = "filename with spaces.txt"
quoted_header_value = quote_header(header_value_with_special_chars)
print(quoted_header_value)
