from werkzeug.wrappers import Request

def get_script_name(environ, start_response):
    request = Request(environ)
    return request.script_root.encode('utf-8')
