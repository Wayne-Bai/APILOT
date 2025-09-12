from werkzeug.utils import secure_filename
# Define the string template
template_string = "Hello, my name is {name} and I am {age} years old."
# Define the values to be inserted into the template string
name = "John"
age = 25
# Format the string using the values
formatted_string = template_string.format(name=name, age=age)
# Print the formatted string
print(formatted_string)
