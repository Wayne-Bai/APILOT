from werkzeug.routing import RequestRedirect

def get_next_path_segment(path_info):
    """Returns the next segment on the PATH_INFO or None if there is none."""
    if path_info is None:
        return None

    segments = path_info.strip('/').split('/')
    if len(segments) > 1:
        return segments[1]

    return None

