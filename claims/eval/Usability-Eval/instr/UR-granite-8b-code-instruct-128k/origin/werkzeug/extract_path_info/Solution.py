from werkzeug.urls import get_path_info

def get_path_info_from_url(environ):
    return get_path_info(environ)
