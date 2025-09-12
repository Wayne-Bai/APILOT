from werkzeug.routing import RequestRedirect
from werkzeug.wrappers import Request

def get_next_segment(request: Request):
    path_info = request.path
    if not path_info:
        return None
    segments = path_info.split('/')
    if segments and segments[0] == '':
        segments.pop(0)
    if segments:
        return segments.pop(0)
    return None

# Example usage:
# request = Request({'PATH_INFO': '/segment1/segment2'})
# next_segment = get_next_segment(request)
# print(next_segment)  # Output: 'segment1'
