
from werkzeug.serving import wsgi_app

def get_next_segment(environ):
    path_info = environ.get('PATH_INFO', '')
    segments = path_info.strip('/').split('/')
    return segments.pop(0) if segments else None
