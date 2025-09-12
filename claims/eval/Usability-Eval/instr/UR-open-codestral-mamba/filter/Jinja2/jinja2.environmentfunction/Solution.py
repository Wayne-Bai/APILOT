from jinja2 import Environment

def render_template(env: Environment, template_file: str, **context) -> str:
    template = env.get_template(template_file)
    return template.render(**context)
