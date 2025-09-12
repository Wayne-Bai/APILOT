# import the necessary module
from werkzeug.wrappers import Request
from werkzeug.routing import Map, Rule

def get_next_segment(environ):
    request = Request(environ)
    url_map = Map([Rule('/<path:path_info>')])

    adapter = url_map.bind_to_environ(environ)
    try:
        matched = adapter.match()
        path_info = matched['path_info'].split('/')
        return path_info[0] if path_info else None
    except:
        return None

# To use the function:
# print(get_next_segment({'PATH_INFO': '/segment1/segment2/segment3'}))
# It will return: segment1
