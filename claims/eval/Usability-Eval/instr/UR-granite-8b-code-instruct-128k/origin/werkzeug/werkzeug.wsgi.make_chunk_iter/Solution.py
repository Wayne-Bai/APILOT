from werkzeug.wsgi import make_line_iter

def make_custom_line_iter(input_string, separator="\n"):
    return make_line_iter(input_string.encode("utf-8"), separator=separator)
