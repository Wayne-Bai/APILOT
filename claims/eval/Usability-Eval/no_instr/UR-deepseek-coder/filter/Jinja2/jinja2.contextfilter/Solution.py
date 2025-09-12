from jinja2 import Environment, FileSystemLoader

def render_template(template_name, **context):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_name)
    return template.render(**context)

def template_decorator(template_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            context = func(*args, **kwargs)
            return render_template(template_name, **context)
        return wrapper
    return decorator

# Example usage
@template_decorator('example.html')
def example_function(data):
    return {'data': data}

# Call the decorated function
result = example_function("Hello, Jinja2!")
print(result)
