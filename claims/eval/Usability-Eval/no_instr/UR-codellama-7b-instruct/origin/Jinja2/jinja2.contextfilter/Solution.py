
from jinja2 import Environment, FileSystemLoader

def render_template(context):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('index.html')
    return template.render(context)
