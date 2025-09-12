from werkzeug import Template

# Create a template object
t = Template('Hello, {{ name }}!')

# Define the context
context = {'name': 'Alice'}

# Format the string using the template
formatted_string = t.render(context)

print(formatted_string)  # Output: Hello, Alice!
