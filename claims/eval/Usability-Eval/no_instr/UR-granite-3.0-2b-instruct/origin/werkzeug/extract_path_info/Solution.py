from werkzeug import Request

def extract_path_info(url_or_env):
    request = Request(url_or_env)
    path_info = request.path_info
    return path_info
