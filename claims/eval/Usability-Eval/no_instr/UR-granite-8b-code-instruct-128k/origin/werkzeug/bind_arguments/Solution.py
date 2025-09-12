from werkzeug.utils import bind_arguments

def my_function(arg1, arg2, arg3):
    """This is my function."""
    print("Arguments passed to the function:")
    print(f"arg1: {arg1}")
    print(f"arg2: {arg2}")
    print(f"arg3: {arg3}")

if __name__ == "__main__":
    args = {"arg1": "Hello", "arg2": "World", "arg3": 123}
    bound_function = bind_arguments(my_function, **args)
    bound_function()
