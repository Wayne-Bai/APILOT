
import werkzeug.formats as formats

# Define a template string with placeholders for variables
template_string = "Hello {name}!"

# Define a dictionary of variables to be formatted into the template string
variables = {"name": "World"}

# Use the `format` method from the `werkzeug.formats` module to format the template string with the variables
formatted_string = formats.format(template_string, **variables)

print(formatted_string)  # Output: Hello World!
