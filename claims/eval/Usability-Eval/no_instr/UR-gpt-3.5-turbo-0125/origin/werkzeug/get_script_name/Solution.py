
from werkzeug.urls import url_unquote

def get_decoded_script_name(environ):
    script_name = environ.get('SCRIPT_NAME', '')
    return url_unquote(script_name)

# Test the function
environ = {'SCRIPT_NAME': '/myapp'}
decoded_script_name = get_decoded_script_name(environ)
print(decoded_script_name)
