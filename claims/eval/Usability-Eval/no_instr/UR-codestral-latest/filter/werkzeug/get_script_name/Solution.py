from werkzeug.wrappers import Request
import urllib.parse

def get_script_name():
    request = Request(environ={})
    script_name = request.environ.get('SCRIPT_NAME', '')
    decoded_script_name = urllib.parse.unquote(script_name)
    return decoded_script_name
