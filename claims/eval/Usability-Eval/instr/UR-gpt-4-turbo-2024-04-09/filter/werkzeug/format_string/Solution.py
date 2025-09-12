from werkzeug.utils import secure_filename

def format_string(template, **kwargs):
    try:
        # Secure the template to avoid path traversal vulnerabilities
        secure_template = secure_filename(template)
        # Format the string using Python's string formatting
        formatted_string = secure_template.format(**kwargs)
        return formatted_string
    except Exception as e:
        return f"Error formatting string: {e}"

# Example usage
template = "Hello, {name}! Welcome to {event}."
print(format_string(template, name="Alice", event="Python Conference"))
