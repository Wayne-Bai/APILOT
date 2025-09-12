
from urllib.parse import unquote

def get_decoded_script_name(environ):
    script_name = environ.get('SCRIPT_NAME', '')
    decoded_script_name = unquote(script_name)
    return decoded_script_name
