from werkzeug.utils import FunctionArgs

def greet(name, age):
    print(f"Hello {name}! You are {age} years old.")

# Create a dict with the function's parameters and values
args = {"name": "Alice", "age": 25}

# Bind the arguments to the function using FunctionArgs
bound_function = FunctionArgs(greet, args).bind()

# Call the bound function with the bound arguments
result = bound_function()

print(result)
