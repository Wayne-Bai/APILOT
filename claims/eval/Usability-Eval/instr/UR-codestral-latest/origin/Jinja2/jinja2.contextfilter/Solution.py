from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('my_template.html')  # Load your template file

# Define your function that accepts the context
def my_decorator(context):
    def wrapped_function():
        # Use context inside this function
        output = template.render(context)
        return output
    return wrapped_function

# Use the function decorator with a context
@my_decorator({'variable1': 'Value1', 'variable2': 'Value2'})
def my_function():
    pass

# Call the function
result = my_function()
print(result)
