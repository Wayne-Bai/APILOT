from werkzeug import Request

def get_next_segment(path_info):
    request = Request.blank(path_info)
    return request.path[1:] if request.path else None
