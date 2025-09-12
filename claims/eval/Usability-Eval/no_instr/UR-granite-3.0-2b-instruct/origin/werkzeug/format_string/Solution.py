from werkzeug import template

# Assuming 'name' is a variable containing the name you want to format
name = "John Doe"

# Create a template object
template_obj = template.Template('''
    Hello, ${name}!
    Your string template has been formatted.
''')

# Render the template with the given data
formatted_string = template_obj.render(name=name)

# Print the formatted string
print(formatted_string)
