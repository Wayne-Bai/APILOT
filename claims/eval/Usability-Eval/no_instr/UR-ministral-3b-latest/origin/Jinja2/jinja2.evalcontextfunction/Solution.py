from jinja2 import Template

def gen_template(context):
    def decorated_function(function):
        def wrapper(*args, **kwargs):
            context = function(**kwargs)
            return function(context, *args, **kwargs)
        return wrapper
    return decorated_function

template = Template("{{ context.description }}")

@gen_template
def render_description(template, context):
    return template.render(description="Python is great programming language")

render_description(template)
