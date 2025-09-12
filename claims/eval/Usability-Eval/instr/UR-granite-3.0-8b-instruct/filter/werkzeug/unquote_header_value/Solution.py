from werkzeug.utils import unquote

def unquote_header_value(header_value):
    return unquote(header_value)
