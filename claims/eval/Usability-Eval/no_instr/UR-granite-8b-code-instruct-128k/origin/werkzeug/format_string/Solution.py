from werkzeug.utils import format_string

# Define your string template
template = "Hello, {name}!"

# Define your input data
data = {"name": "John"}

# Format the string using the input data
formatted_string = format_string(template, **data)

# Print the formatted string
print(formatted_string)
