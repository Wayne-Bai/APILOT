from jinja2 import Environment, FileSystemLoader

def passed_context_decorator(func):
    def wrapper(env, template_name, context):
        func(env, template_name, context)
        return env.get_template(template_name).render(context)
    return wrapper

class PassingContext:
    def __init__(self, template_path):
        self.env = Environment(loader=FileSystemLoader(template_path))

    @passed_context_decorator
    def render_with_context(self, template_name, context):
        pass

# Example usage
template_path = 'templates'
passing_context = PassingContext(template_path)

template_name = 'example_template.html'
context = {
    'name': 'World',
    'message': 'Hello'
}

print(passing_context.render_with_context(template_name, context))
