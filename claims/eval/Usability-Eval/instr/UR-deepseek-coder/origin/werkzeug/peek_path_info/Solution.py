from werkzeug.routing import RequestRedirect, RoutingException
from werkzeug.wrappers import Request

def get_next_segment(request: Request):
    path_info = request.path
    if not path_info or path_info == '/':
        return None
    segments = path_info.strip('/').split('/')
    if segments:
        return segments[0]
    return None
