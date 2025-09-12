import werkzeug

def get_script_name():
    return werkzeug.routing.BaseConverter.to_python(environ.get("SCRIPT_NAME", ""))
