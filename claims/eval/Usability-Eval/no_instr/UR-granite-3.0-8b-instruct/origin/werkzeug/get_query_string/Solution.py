from werkzeug.utils import get_query_arg

def get_query_string(environ):
    query_string = get_query_arg(environ, 'QUERY_STRING')
    return query_string
