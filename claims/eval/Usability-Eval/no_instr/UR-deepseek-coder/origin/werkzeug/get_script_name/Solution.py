from werkzeug.http import parse_options_header
from werkzeug.urls import iri_to_uri

def get_script_name(environ):
    script_name = environ.get('SCRIPT_NAME', '')
    if isinstance(script_name, bytes):
        script_name = script_name.decode('latin1')
    return iri_to_uri(script_name)
