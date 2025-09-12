from werkzeug.utils import secure_filename

# Example usage of werkzeug's secure_filename function
filename = "my_document.txt"
secure_name = secure_filename(filename)

# Printing the secured filename
print("The secure filename is:", secure_name)

# String-template formatting a string without using werkzeug's outdated APIs
template = "Hello, {name}! Welcome to {place}."
formatted_string = template.format(name="Alice", place="Wonderland")

# Printing the formatted string
print("Formatted string:", formatted_string)
