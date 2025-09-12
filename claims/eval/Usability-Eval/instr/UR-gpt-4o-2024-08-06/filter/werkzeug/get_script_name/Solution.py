from werkzeug.datastructures import EnvironHeaders
from werkzeug.urls import url_unquote

def get_script_name(environ):
    script_name = environ.get('SCRIPT_NAME', '')
    return url_unquote(script_name)

# Example Usage:
# environ = {...}  # This would be your WSGI environment dict
# print(get_script_name(environ))
