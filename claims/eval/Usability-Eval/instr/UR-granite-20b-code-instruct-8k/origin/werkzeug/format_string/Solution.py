import werkzeug

def format_string(string, *args, **kwargs):
    return werkzeug.utils.format_string(string, *args, **kwargs)