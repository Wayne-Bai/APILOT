from werkzeug import templates

# Create a template object
template = templates.Template('Hello, $name!')

# Render the template with a dictionary as values
values = {'name': 'John'}

# Use the render method to replace placeholders with values
rendered_template = template.render(values)

print(rendered_template)
