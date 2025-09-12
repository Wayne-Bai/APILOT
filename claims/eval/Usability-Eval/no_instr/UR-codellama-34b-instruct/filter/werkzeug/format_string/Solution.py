
import werkzeug

# Create a template string with placeholders for values
template = "Hello, my name is {name} and I am {age} years old."

# Define a dictionary of values to fill in the placeholders
values = {"name": "John", "age": 30}

# Create a Template object from the template string
tpl = werkzeug.Template(template)

# Fill in the placeholders with the values and get the formatted string
formatted_string = tpl.render(**values)

print(formatted_string) # Output: Hello, my name is John and I am 30 years old.
