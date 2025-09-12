from werkzeug.utils import cached_property

def bind_arguments(func):
    def wrapper(*args, **kwargs):
        arg_dict = {}
        signature = inspect.signature(func)
        for index, (name, param) in enumerate(signature.parameters.items()):
            if index < len(args):
                arg_dict[name] = args[index]
            elif name in kwargs:
                arg_dict[name] = kwargs[name]
            else:
                arg_dict[name] = param.default if param.default is not param.empty else None
        return func(**arg_dict)
    return wrapper
