from werkzeug.wrappers import Request

def get_next_path_segment(environ):
    request = Request(environ)
    path_info = request.path_info.strip('/')
    segments = path_info.split('/')
    
    try:
        next_segment = segments[0] if segments else None
    except IndexError:
        next_segment = None
    
    return next_segment
