from jinja2 import Environment, FileSystemLoader, Template

def render_template_with_context(template_path, context):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_path)
    return template.render(context)

# Example usage
context = {
    'name': 'Alice',
    'age': 30
}

rendered_output = render_template_with_context('template.html', context)
print(rendered_output)
