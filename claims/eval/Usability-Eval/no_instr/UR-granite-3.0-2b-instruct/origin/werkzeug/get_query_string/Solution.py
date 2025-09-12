from werkzeug import get_environ

def get_query_string():
    query_string = get_environ('QUERY_STRING')
    return query_string
