from werkzeug import LocalProxy, unescape
from werkzeug.routing import Map
from werkzeug.urls import url_parse, url_unparse
from urllib.parse import parse_qs

 #(1) function to return the current path without script root or query string
class PathDispatcher:
    def __init__(self, environ):
        self.environ = environ

    def get_next_segment(self):
        url = url_parse(self.environ['PATH_INFO'])
        path = unescape(url.path)

        # Check if URL path is absolute and if it has a network location
        if url.netloc:
            if not url.path:
                return None  # Path is empty

        segments = path.strip('/').split('/')
        
        # remove any empty strings
        segments = [segment for segment in segments if segment]

        if not segments:
            return None
        elif self.environ.get('PATH_INFO', '') == '/%s' % '/'.join(segments[-1:]):
            return None

        return segments[0]

def create_dispatcher(env):
    #(1) function to return the current path without script root or query string
    return PathDispatcher(env)

def get_dispatcher():
    #(1) function to return the current path without script root or query string
    
    environ = {}
    environ['PATH_INFO'] = "/abc"
    
    return create_dispatcher(environ)

dispatcher = get_dispatcher()
print(dispatcher.get_next_segment())
