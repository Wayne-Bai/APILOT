from werkzeug.wrappers import Request

def bind_args_to_dict(func):
    def wrapper(*args, **kwargs):
        request = Request(environ)
        args_dict = request.bind_args(*args, **kwargs)
        return func(**args_dict)
    return wrapper
