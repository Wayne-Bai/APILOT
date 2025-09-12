from werkzeug import http_headers as headers

# Define a function to quote a header value if necessary
def quote_header(header_name, value):
    """
    Quotes a header value if necessary.

    :param header_name: The name of the header.
    :param value: The value of the header.
    :return: The quoted header value.
    """
    quoted_value = ""
    for char in value:
        if char in '\'"<>#:\\proxies' or char == '"':
            # Use the standard escaping for special characters
            if char == '"':
                quoted_value += '\\"'
            else:
                quoted_value += '\\'
                quoted_value += char
        else:
            # Non-special characters are left unchanged
            quoted_value += char
    return f"{header_name}: {quoted_value}"

# Usage example
header_name = "User-Agent"
value = "Mozilla/5.0 Gecko/20100101 Firefox/60.0"
quoted_header = quote_header(header_name, value)
print(quoted_header)
