from werkzeug.utils import unquote_header_value

def unquote_header(header_value):
    return unquote_header_value(header_value)
