from werkzeug import utils
from werkzeug.routing import Route

def get_next_segment(path_info):
    segments = path_info.split('/')
    if len(segments) > 1:
        return utils.pointer(segments[-2])
    return None

# Example usage
path_info = "/example/path"
next_segment = get_next_segment(path_info)
print(next_segment)  # Output: /example
