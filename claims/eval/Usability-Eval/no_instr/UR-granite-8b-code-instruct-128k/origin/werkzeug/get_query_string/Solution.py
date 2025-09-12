from werkzeug.utils import get_query_string

def get_query_string_from_wsgi_env(environ):
    return get_query_string(environ)
