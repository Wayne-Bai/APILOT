from werkzeug import Request

def get_next_segment(path_info):
    request = Request.blank(path_info)
    path_info_segments = path_info.split("/")
    if path_info_segments:
        return path_info_segments[0]
    else:
        return None
