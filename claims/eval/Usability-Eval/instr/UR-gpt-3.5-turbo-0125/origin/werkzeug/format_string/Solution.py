
from werkzeug.utils import format_string

def string_template_format(input_string, **kwargs):
    return format_string(input_string, kwargs)

# Example usage
template = "Hello, ${name}! You have ${count} new messages."
formatted_string = string_template_format(template, name="Alice", count=3)
print(formatted_string)
