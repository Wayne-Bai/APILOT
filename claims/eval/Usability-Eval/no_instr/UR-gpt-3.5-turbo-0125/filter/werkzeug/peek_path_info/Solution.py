
from werkzeug.urls import url_parse

def get_next_segment(path_info):
    path = url_parse(path_info).path
    segments = path.strip('/').split('/')
    if len(segments) > 1:
        return segments[1]
    else:
        return None

# Example Usage
path_info = '/segment1/segment2/segment3'
next_segment = get_next_segment(path_info)
print(next_segment)
