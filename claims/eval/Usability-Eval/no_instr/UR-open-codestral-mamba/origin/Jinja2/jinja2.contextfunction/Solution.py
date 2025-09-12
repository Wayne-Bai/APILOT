from jinja2 import Environment, FileSystemLoader

# Define a context
context = {
    'name': 'John Doe',
    'age': 30,
}

# Define the decorated function
def render_template(template_name, **context):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_name)
    output = template.render(context)
    return output

# Call the decorated function and render the template
output = render_template('user_info.html', **context)
print(output)
