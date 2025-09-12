from werkzeug.http import http_date

def get_script_name(environ):
    script_name = environ.get('SCRIPT_NAME', '')
    return script_name.encode('latin1').decode('utf-8')
