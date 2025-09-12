from jinja2 import Environment, FileSystemLoader

# Create a Jinja2 environment and load the template
env = Environment()
loader = FileSystemLoader("templates")
template = env.get_template("my_template.html")

# Define the EvalContext
class EvalContext:
    def __init__(self, data):
        self.data = data

# Define a function to be decorated
def my_function(context):
    # Access the data from the EvalContext
    data = context.data
    # Process the data and return a result
    return f"Data: {data}"

# Decorate the function with the EvalContext
def decorate_with_evalcontext(func):
    def wrapper(context):
        # Pass the EvalContext as the first argument to the function
        result = func(EvalContext(context))
        # Return the result
        return result
    return wrapper

# Decorate the function with the EvalContext
my_function = decorate_with_evalcontext(my_function)

# Render the template with the EvalContext
result = template.render(context=EvalContext({"data": "Hello, world!"}))

# Print the result
print(result)
