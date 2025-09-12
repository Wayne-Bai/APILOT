from werkzeug.utils import format_string

# Example template string
template = "Hello, {name}! Your email is {email}."

# Data to be formatted into the template
data = {
    'name': 'John Doe',
    'email': 'john.doe@example.com'
}

# Format the string using the template and data
formatted_string = format_string(template, **data)

print(formatted_string)
