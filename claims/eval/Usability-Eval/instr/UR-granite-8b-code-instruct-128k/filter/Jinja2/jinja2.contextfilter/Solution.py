from jinja2 import Environment, FunctionLoader
# Define your template
template = """
Hello, {{ name }}!
"""
# Define your context
context = {
    'name': 'John'
}
# Create a Jinja2 environment
env = Environment(loader=FunctionLoader(lambda x: template))
# Render the template with the context
output = env.from_string(template).render(context)
# Print the output
print(output)
