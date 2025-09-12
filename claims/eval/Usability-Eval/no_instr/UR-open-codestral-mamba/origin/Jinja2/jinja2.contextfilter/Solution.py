from jinja2 import Environment, PackageLoader, select_autoescape

# Load the environment with the select autoescape feature
env = Environment(
    loader=PackageLoader('your_package_name', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

# Load the template you want to use
template = env.get_template('your_template.html')

# Prepare the context, which will be passed to the template
context = {
    'key1': 'value1',
    'key2': 'value2',
    # Add more key-value pairs as needed
}

# Render the template with the given context
output = template.render(context)

# Now, the output variable contains the final HTML
