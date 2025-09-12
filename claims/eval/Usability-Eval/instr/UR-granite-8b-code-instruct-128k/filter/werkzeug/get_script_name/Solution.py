from werkzeug.http import parse_script_header
from werkzeug.urls import path_match
def get_script_name(environ):
    script_name = environ.get('SCRIPT_NAME', '')
    if script_name:
        script_name = parse_script_header(script_name)[1]
    if not script_name or script_name == '/':
        return ''
    return script_name
def match_path(environ, path):
    script_name = get_script_name(environ)
    match = path_match(script_name + path, environ['PATH_INFO'])
    return match.group(0)
