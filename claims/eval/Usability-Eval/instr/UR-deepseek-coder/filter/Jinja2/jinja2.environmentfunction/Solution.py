from jinja2 import Environment, FileSystemLoader

def render_template(env, template_name, **context):
    template = env.get_template(template_name)
    return template.render(**context)

def template_decorator(template_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            env = args[0]  # The first argument is the Environment
            context = func(*args, **kwargs)
            return render_template(env, template_name, **context)
        return wrapper
    return decorator

# Example usage
env = Environment(loader=FileSystemLoader('templates'))

@template_decorator('example.html')
def my_view(env):
    return {'name': 'World'}

# Call the decorated function
result = my_view(env)
print(result)
