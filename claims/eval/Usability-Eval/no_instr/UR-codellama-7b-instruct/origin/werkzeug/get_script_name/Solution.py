from werkzeug.wrappers import Request, Response

def get_script_name(environ):
    """Returns the SCRIPT_NAME value from the WSGI environment."""
    script_name = environ['SCRIPT_NAME']
    if script_name:
        return script_name
    else:
        raise ValueError('No SCRIPT_NAME value found in WSGI environment')
