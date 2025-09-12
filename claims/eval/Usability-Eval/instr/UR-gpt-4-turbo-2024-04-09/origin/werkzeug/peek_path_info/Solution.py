from werkzeug.urls import url_parse

def get_next_path_segment(path_info):
    # Parse the URL to get the path
    path_segments = url_parse(path_info).path.strip('/').split('/')
    
    # Return the first segment or None if there is no segment
    return path_segments[0] if path_segments else None
