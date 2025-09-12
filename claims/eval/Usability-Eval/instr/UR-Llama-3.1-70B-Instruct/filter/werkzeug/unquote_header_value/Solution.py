from werkzeug.datastructures import UnquoteError, unquote_header_value as _unquote_header_value

def unquote_header_value(s, charset='utf-8', errors='replace'):
    """
    Unquotes a header value.  (Replaces %xx escapes in a `-_LEN*` or `LEN*` header value.)

    :param s: The header value to unquote.
    :param charset: The charset to use for the header value.
    :param errors: The error handling on decode.
    :return: The unquoted header value.
    :rtype: unicode
    """
    if isinstance(s, bytes):
        if '%' not in s:
            return s.decode(charset, errors)
        try:
            return _unquote_header_value(s.decode(charset, errors)).encode(charset, errors).decode()
        except UnicodeDecodeError:
            raise UnquoteError('Invalid header value %r' % s)
    if '%' not in s:
        return s
    return _unquote_header_value(s)

# Example usage:
quoted_header_value = "%3F"  # Quoted header value (question mark)
unquoted_header_value = unquote_header_value(quoted_header_value)
print("Unquoted Header Value:", unquoted_header_value)  # Output:?
