from werkzeug import get_environ

def get_query_string():
    environ = get_environ()
    return environ.get('QUERY_STRING')
