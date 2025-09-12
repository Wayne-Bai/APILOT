from werkzeug.utils import bind_arguments

def example_function(a, b, c=3):
    return a + b + c

args = {'a': 1, 'b': 2, 'c': 4}
bound_args = bind_arguments(example_function, **args)

print(bound_args)
