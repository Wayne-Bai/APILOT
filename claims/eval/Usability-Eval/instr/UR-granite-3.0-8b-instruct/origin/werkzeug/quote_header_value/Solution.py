from werkzeug.utils import secure_filename

def quote_header_value(value):
    if '/' in value or ' ' in value or '\n' in value:
        return "'" + value + "'"
    return value
