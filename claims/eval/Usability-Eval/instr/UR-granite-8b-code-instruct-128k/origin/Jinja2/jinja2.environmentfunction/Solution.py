from jinja2 import Environment

def render_template(template, environment):
    return environment.from_string(template)

template = '''
Hello, {{ name }}!
'''

env = Environment()
rendered_template = render_template(template, env)
print(rendered_template.render(name='John'))
