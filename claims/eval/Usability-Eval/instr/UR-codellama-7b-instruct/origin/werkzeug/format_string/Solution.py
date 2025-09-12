
from werkzeug import templates

# Define the template and variables
template = 'Hello, ${name}!'
variables = {'name': 'John'}

# Perform the string formatting
result = templates.format_string(template, variables)

print(result) # Output: Hello, John!
