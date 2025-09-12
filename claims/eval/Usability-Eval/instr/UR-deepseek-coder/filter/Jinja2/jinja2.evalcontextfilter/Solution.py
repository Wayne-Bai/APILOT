from jinja2 import Environment, FileSystemLoader, Template, EvalContext

def render_with_context(template_path, context):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_path)
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            eval_context = EvalContext(template, context)
            return func(eval_context, *args, **kwargs)
        return wrapper
    
    return decorator

# Example usage
@render_with_context('example.html', {'key': 'value'})
def my_function(eval_context, additional_arg):
    rendered_template = eval_context.template.render(eval_context.context)
    print(rendered_template)
    print(additional_arg)

my_function('additional argument')
