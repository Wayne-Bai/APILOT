from jinja2 import Template

def render_template_with_env(template_str, environment):
    template = Template(template_str)
    rendered = template.render(environment=environment)
    print(rendered)
