from werkzeug.utils import secure_filename

def format_string(template, **kwargs):
    """Format a string using a template and keyword arguments."""
    return template.format(**kwargs)

# Example usage:
template = "Hello, {}! Today is {}."
name = "Alice"
date = "2022-01-01"
formatted_string = format_string(template, name=name, date=date)
print(formatted_string)
