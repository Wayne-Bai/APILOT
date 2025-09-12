from jinja2 import Environment, FileSystemLoader, Template, EvalContext

def render_template_with_context(template_path, context):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_path)
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(EvalContext(context), *args, **kwargs)
            return template.render(context)
        return wrapper
    
    return decorator

# Example usage:
@render_template_with_context('example.html', {'name': 'Alice'})
def example_function(eval_context):
    # Access the context via eval_context
    print(eval_context.name)
    return "Processed"

# Call the decorated function
example_function()
