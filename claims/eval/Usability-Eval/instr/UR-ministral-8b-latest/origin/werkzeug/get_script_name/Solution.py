from werkzeug import httputil

def get_script_name():
    script_name = httputil.decode_params(httputil.params_from_environ())
    return script_name
