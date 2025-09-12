from jinja2 import Environment, FileSystemLoader, Template

def render_template_with_context(template_path, context):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_path)
    return template.render(context)

def template_decorator(template_path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            context = func(*args, **kwargs)
            return render_template_with_context(template_path, context)
        return wrapper
    return decorator

# Example usage
@template_decorator('example.html')
def example_function(data):
    return {'data': data}

# Call the decorated function
result = example_function("Hello, Jinja2!")
print(result)
