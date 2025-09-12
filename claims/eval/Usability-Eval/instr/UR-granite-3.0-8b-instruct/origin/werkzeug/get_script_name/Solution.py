from werkzeug.utils import secure_filename

def get_script_name(environ):
    script_name = environ.get('SCRIPT_NAME', '')
    if script_name:
        script_name = script_name.decode('utf-8')
    return script_name
