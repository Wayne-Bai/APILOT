from jinja2 import Environment, FileSystemLoader

def render_template(template_name, context):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_name)
    output = template.render(context)
    return output

# Usage
template_name = 'my_template.html'
context = {
    'context_variable1': 'value1',
    'context_variable2': 'value2',
    # Add as many variables as you need
}
rendered_template = render_template(template_name, context)
print(rendered_template)
