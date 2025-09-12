from werkzeug.utils import secure_filename

def format_string(template, **kwargs):
    for key, value in kwargs.items():
        template = template.replace(f'{{{{ {key} }}}}', str(value))
    return template

# Example usage
template = "Hello, {{ name }}! Welcome to {{ place }}."
formatted_string = format_string(template, name="Alice", place="Wonderland")
print(formatted_string)  # Output: Hello, Alice! Welcome to Wonderland.
