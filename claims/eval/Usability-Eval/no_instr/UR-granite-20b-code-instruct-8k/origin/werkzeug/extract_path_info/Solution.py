import werkzeug

def extract_path_info(url_or_wsgi_environment):
    request = werkzeug.wrappers.Request(url_or_wsgi_environment)
    return request.path
