from werkzeug.utils import format_string

template = "Hello, {name}!"
output = format_string(template, name="Alice")
print(output)  # Output: Hello, Alice!
