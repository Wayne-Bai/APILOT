from werkzeug.utils import secure_filename

def format_string(template, **kwargs):
    return template.format(**kwargs)

# Example usage:
template = "Hello, {}!"
name = "Alice"
formatted_string = format_string(template, name=name)
print(formatted_string)  # Output: Hello, Alice!
