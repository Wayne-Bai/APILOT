from werkzeug.urls import iri_to_uri

def get_script_name(environ):
    """Returns the SCRIPT_NAME from the WSGI environment and properly decodes it."""
    script_name = environ.get('SCRIPT_NAME', '')
    return iri_to_uri(script_name)

# Example usage within a WSGI environment
# environ = {'SCRIPT_NAME': '/your_script_name'}
# print(get_script_name(environ))
