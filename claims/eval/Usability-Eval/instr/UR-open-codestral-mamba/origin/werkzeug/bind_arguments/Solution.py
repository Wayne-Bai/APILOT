from werkzeug.datastructures import ImmutableMultiDict

def my_function(arg1, arg2, arg3):
    # Place your function code here
    pass

args = (1, 2, 3)  # Example arguments
args_dict = ImmutableMultiDict(zip(my_function.__code__.co_varnames, args))

# Example usage of args_dict in your function
my_function(**args_dict)
