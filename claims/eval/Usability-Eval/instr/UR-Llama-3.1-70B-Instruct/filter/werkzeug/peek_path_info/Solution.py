from werkzeug import unquote
from werkzeug.urls import url_parse, url_unparse

def get_next_segment(environ):
    """
    Returns the next segment on the PATH_INFO or None if there is none.

    :param environ: The WSGI environment.
    """
    path_info = environ.get('PATH_INFO')
    if path_info is None:
        return None

    # Split the PATH_INFO into segments
    segments = path_info.strip('/').split('/')

    # If there are no segments, return None
    if len(segments) == 0:
        return None

    # Check if the last segment is empty, if so remove it
    if segments[-1] == '':
        segments.pop()

    # If there are no segments left after removing the empty segment, return None
    if len(segments) == 0:
        return None

    # Return the next segment
    return unquote(segments[0])

def get_next_segment_from_path(path):
    """
    Returns the next segment on the path or None if there is none.

    :param path: The path to get the next segment from.
    """
    scheme, netloc, path, params, query, fragment = url_parse(path)
    segments = path.strip('/').split('/')
    
    # If there are no segments, return None
    if len(segments) == 0:
        return None

    # Check if the last segment is empty, if so remove it
    if segments[-1] == '':
        segments.pop()

    # If there are no segments left after removing the empty segment, return None
    if len(segments) == 0:
        return None

    # Return the next segment
    return unquote(segments[0])
