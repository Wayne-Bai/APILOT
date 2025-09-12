
from werkzeug import Request, Response

def get_next_segment(path: str) -> str | None:
    # Get the current path info
    request = Request.from_environ()
    current_path_info = request.path_info

    # Check if there is a next segment
    next_segment = current_path_info.split('/')[1]
    if next_segment == '':
        return None

    # Return the next segment
    return next_segment
