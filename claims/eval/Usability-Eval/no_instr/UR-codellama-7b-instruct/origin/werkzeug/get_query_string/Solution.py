
from werkzeug import Request

def get_query_string(wsgi_env):
    request = Request(wsgi_env)
    return request.GET.get("QUERY_STRING")
