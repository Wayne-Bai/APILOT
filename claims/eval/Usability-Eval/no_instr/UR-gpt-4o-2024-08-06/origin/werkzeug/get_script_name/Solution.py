from werkzeug.wsgi import get_current_url
from werkzeug.urls import url_decode

def get_script_name(environ):
    script_name = environ.get('SCRIPT_NAME', '')
    # Decoding the script name properly
    decoded_script_name = url_decode(script_name)
    return decoded_script_name
