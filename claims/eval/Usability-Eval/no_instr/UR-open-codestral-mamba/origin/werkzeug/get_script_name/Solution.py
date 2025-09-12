from werkzeug.wsgi import get_script_name

def get_script_name_from_wsgi_env(environ):
    return get_script_name(environ)
