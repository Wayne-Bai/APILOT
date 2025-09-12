from werkzeug.http import parse_options_header

def unquote_header_value(value):
    """
    Unquote a header value that may be quoted.

    :param value: The header value as a string.
    :return: The unquoted header value.
    """
    unquoted_value, options = parse_options_header(value)
    return unquoted_value

# Example usage
quoted_value = '"Hello, World!"'
unquoted_value = unquote_header_value(quoted_value)
print(unquoted_value)  # Output: Hello, World!
