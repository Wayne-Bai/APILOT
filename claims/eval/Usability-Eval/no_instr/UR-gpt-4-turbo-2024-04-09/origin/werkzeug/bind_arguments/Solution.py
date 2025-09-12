from werkzeug.datastructures import ImmutableMultiDict

def bind_arguments(func, *args, **kwargs):
    arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]
    bound_args = {}
    
    # Binding positional arguments
    for name, value in zip(arg_names, args):
        bound_args[name] = value

    # Binding keyword arguments
    bound_args.update(kwargs)

    # Filtering out any extra arguments that are not in the function signature
    bound_args = {key: bound_args[key] for key in bound_args if key in arg_names}

    return ImmutableMultiDict(bound_args)

# Example usage:
def example_function(a, b, c):
    print("a:", a, "b:", b, "c:", c)

# Binding the arguments
bound_args = bind_arguments(example_function, 1, 2, c=3)
print("Bound Arguments:", bound_args)
