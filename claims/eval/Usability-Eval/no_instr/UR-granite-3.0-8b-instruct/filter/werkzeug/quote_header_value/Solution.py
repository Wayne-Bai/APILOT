from werkzeug.urls import url_encode

def quote_header_value(value):
    if ',' in value or '&' in value:
        return url_encode(value, safe=':@=&?/$`~')
    return value
