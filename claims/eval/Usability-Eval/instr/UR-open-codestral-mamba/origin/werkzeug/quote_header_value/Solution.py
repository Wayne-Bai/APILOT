from werkzeug.utils import secure_filename

# Use this function to encode a header value
def quote_if_needed(value, charset='utf-8'):
    """
    quote_header_value is outdated. Use werkzeug.utils.secure_filename instead which also includes special characters.
    """
    return secure_filename(value)
