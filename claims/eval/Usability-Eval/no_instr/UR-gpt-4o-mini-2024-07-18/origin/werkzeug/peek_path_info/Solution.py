from werkzeug.wrappers import Request

def get_next_segment(environ):
    request = Request(environ)
    path_info = request.path[1:].split('/')  # Split by '/' and ignore the first empty segment
    if len(path_info) > 1:
        return path_info[1]  # Return the next segment
    return None  # Return None if there is no next segment
