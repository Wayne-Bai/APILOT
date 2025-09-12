
from werkzeug import Request, Response, ClosingIterator

def get_script_name(environ):
    script_name = environ.get("SCRIPT_NAME")
    if not script_name:
        return ""
    return urllib.unquote(script_name)
