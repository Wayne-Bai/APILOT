from werkzeug.urls import url_parse

def get_query_string(environ):
    query_string = url_parse(environ['PATH_INFO']).query
    return query_string
