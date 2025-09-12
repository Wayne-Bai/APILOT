
from jinja2 import Template, Environment

# Create an environment object
env = Environment()

# Load the template file and pass it to the env object
template_file = "example.html"
template = env.get_template(template_file)

# Decorate the function that will be called when rendering the template
@env.global_function
def my_function():
    return "Hello, world!"

# Render the template using the decorated function
output = template.render(my_function=my_function)
print(output)
