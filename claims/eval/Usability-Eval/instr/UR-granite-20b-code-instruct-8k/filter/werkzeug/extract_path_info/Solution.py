
from werkzeug import Request

def extract_path_info(url_or_environ):
    request = Request(url_or_environ)
    return request.path
