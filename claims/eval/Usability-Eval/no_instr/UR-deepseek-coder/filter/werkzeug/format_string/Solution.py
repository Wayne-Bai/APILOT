from werkzeug.utils import format_string

template = "Hello, {name}! Your email is {email}."
data = {"name": "John Doe", "email": "john.doe@example.com"}

formatted_string = format_string(template, **data)
print(formatted_string)
