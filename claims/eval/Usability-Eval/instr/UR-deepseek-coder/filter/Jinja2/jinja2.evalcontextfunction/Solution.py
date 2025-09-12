from jinja2 import Environment, FileSystemLoader, Template, EvalContext

def render_with_context(template_path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            env = Environment(loader=FileSystemLoader('templates'))
            template = env.get_template(template_path)
            context = func(*args, **kwargs)
            rendered_template = template.render(context, eval_ctx=EvalContext(env))
            return rendered_template
        return wrapper
    return decorator

# Example usage:
@render_with_context('example.html')
def example_function(data):
    return {'data': data}

# Call the decorated function
result = example_function("Sample Data")
print(result)
