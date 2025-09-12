from werkzeug.utils import quote_header_value

def quote_header_value_if_necessary(header_value):
    return quote_header_value(header_value)
