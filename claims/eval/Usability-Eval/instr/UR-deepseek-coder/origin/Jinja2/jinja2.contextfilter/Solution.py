from jinja2 import Template

def render_template(template_string, **context):
    template = Template(template_string)
    return template.render(**context)

@render_template
def my_function(context):
    return "Hello, {{ name }}!"

# Example usage
result = my_function(name="World")
print(result)  # Output: Hello, World!
