from werkzeug import unescape

def get_script_name(environ):
    """
    Returns the SCRIPT_NAME from the WSGI environment and properly decodes it.
    
    :param environ: The WSGI environment.
    """
    return unescape(environ.get('SCRIPT_NAME', ''))

# Usage example
if __name__ == "__main__":
    # Simulating a WSGI environment
    environ = {'SCRIPT_NAME': '/my-app'}
    print(get_script_name(environ))
