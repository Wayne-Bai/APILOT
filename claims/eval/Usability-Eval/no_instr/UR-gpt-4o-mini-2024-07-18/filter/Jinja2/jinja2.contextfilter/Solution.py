from jinja2 import Template

def render_template(template_string, context):
    template = Template(template_string)
    return template.render(context)

# Example usage
template_string = "Hello, {{ name }}!"
context = {"name": "Alice"}
output = render_template(template_string, context)
print(output)  # Output: Hello, Alice!
