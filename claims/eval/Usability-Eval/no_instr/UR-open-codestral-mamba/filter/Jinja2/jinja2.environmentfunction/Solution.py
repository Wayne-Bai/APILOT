from jinja2 import Environment, FileSystemLoader

def render_template(template_file, context):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_file)
    return template.render(context)

# Example usage
render_template('template.html', {'key': 'value'})
