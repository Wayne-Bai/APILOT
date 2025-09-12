from werkzeug.urls import url_decode

def get_script_name(environ):
    script_name = environ.get('SCRIPT_NAME', '')
    return url_decode(script_name)
