from jinja2 import Environment, Template

def pass_context_decorator(func):
    def wrapper(context, *args, **kwargs):
        return func(context, *args, **kwargs)
    return wrapper

# Example usage inside a Jinja2 template
env = Environment()

@env.contextfunction
@pass_context_decorator
def get_data(context, key):
    return context[key]

template_src = "{{ get_data('name') }}"
template = env.from_string(template_src)

# Render the template with some context data
rendered_output = template.render(name="Alice")
print(rendered_output)
