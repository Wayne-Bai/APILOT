
from werkzeug.urls import url_parse

def get_path_info(url_or_wsgi_env):
    if isinstance(url_or_wsgi_env, str):
        parsed_url = url_parse(url_or_wsgi_env)
        return parsed_url.path
    elif isinstance(url_or_wsgi_env, dict):
        return url_or_wsgi_env.get('PATH_INFO', '')
    else:
        raise TypeError('Invalid input type. Expected str or dict.')
