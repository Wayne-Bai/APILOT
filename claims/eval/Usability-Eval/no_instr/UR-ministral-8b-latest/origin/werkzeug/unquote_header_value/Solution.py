import werkzeug
import re

def unquote_header_value(value):
    return werkzeug.url.url_quote(value)

value_to_unquote = '='
print(unquote_header_value(value_to_unquote))
