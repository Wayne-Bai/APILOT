from jinja2 import Template

# Create a decorator function
def pass_context_as_first_arg(fn):
    def wrapper(context, *args, **kwargs):
        return fn(context, *args, **kwargs)
    return wrapper

# Create a sample function to demonstrate the decorator usage
@pass_context_as_first_arg
def render_template(context, template_string):
    template = Template(template_string)
    return template.render(context)

# Example usage
context_data = {
    'name': 'Alice',
    'age': 30
}

template_str = "Name: {{ name }}; Age: {{ age }}"
output = render_template(context_data, template_str)
print(output)
