from jinja2 import Environment, FileSystemLoader, pass_context

# Set up the Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

@pass_context
def my_function(context, value):
    # You can now access the context inside this function
    return context['user'] + value

# Register the custom function in the environment
env.filters['my_function'] = my_function

# Example usage
template = env.get_template('example_template.html')
output = template.render(user='John Doe', value=' is logged in.')
print(output)
