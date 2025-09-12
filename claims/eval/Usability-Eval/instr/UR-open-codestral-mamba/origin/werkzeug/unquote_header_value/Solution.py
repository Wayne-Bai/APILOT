from werkzeug.http import unquote_etag, unquote_if_zipped, unquote_http_value

def unquote_header_value(value):
    return unquote_http_value(value)
