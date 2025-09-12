from jinja2 import Template

def pass_context(func):
    def wrapper(context, *args, **kwargs):
        return func(context, *args, **kwargs)
    return wrapper

@pass_context
def render_template(context, template_string):
    template = Template(template_string)
    return template.render(context)

# Example usage:
context_data = {"name": "John"}
template_str = "Hello, {{ name }}!"
print(render_template(context_data, template_str))
