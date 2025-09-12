from jinja2 import Template

def pass_context_to_function(template_str, context):
    template = Template(template_str)
    rendered_content = template.render(context)
    return rendered_content

# Example Usage
template_str = """
<p>User name: {{ user.name }}</p>
<p>User email: {{ user.email }}</p>
"""

context = {
    'user': {
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }
}

rendered_output = pass_context_to_function(template_str, context)
print(rendered_output)
