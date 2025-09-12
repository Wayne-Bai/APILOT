from werkzeug.utils import args_to_dict

def my_function(a, b, c):
    # do something with the arguments
    pass

# call the function with some arguments
result = my_function('foo', 'bar', c='baz')

# bind the arguments into a dictionary using args_to_dict
args = args_to_dict(result)
print(args)  # {'a': 'foo', 'b': 'bar', 'c': 'baz'}
