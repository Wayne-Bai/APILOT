from werkzeug.urls import url_parse

def extract_path_info(url_or_environ):
    if isinstance(url_or_environ, dict):
        # Assume it's a WSGI environment
        path_info = url_or_environ.get('PATH_INFO', '')
    else:
        # Assume it's a URL string
        parsed_url = url_parse(url_or_environ)
        path_info = parsed_url.path
    
    return path_info
