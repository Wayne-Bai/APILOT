from werkzeug.urls import uri_to_iri

def get_script_name(environ):
    """
    Extracts and decodes the SCRIPT_NAME from the WSGI environment.
    
    :param environ: The WSGI environment dictionary.
    :return: The decoded SCRIPT_NAME.
    """
    script_name = environ.get('SCRIPT_NAME', '')
    return uri_to_iri(script_name)
