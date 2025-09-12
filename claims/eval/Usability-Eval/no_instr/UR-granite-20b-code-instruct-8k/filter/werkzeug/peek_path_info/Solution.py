from werkzeug.routing import PathRouting

path_routing = PathRouting()

def get_next_segment(path_info):
    return path_routing.match(path_info)[1]
