from werkzeug.utils import escape
from jinja2 import Template

# A function to format a string using the Jinja2 template engine
def format_string_with_template(template_string, context):
    template = Template(template_string)
    return template.render(context)

# Example usage
user_string = "This is a string: Hello World! How are you doing today?"
context = {"name": "John", "age": 30}
formatted_string = format_string_with_template(user_string, context)
print(formatted_string)  # Output: This is a string: Hello World! How are you doing today?
