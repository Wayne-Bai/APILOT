from werkzeug.utils import escape

def format_string(template, **kwargs):
    # Escape any user-provided content to prevent XSS attacks
    sanitized_kwargs = {key: escape(value) for key, value in kwargs.items()}
    return template.format(**sanitized_kwargs)

# Example usage
template = "Hello, {name}. Welcome to {place}!"
formatted_string = format_string(template, name="Alice", place="Wonderland")
print(formatted_string)  # Output: Hello, Alice. Welcome to Wonderland!
