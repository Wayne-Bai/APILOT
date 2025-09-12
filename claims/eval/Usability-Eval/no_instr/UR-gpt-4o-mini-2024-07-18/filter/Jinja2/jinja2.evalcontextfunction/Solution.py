from jinja2 import Environment, Template

def eval_context_decorator(func):
    def wrapper(eval_context, *args, **kwargs):
        return func(eval_context, *args, **kwargs)
    return wrapper

@eval_context_decorator
def my_render_function(eval_context):
    return f"Rendering with context: {eval_context}"

# Create a Jinja2 environment and template
env = Environment()
template = env.from_string("{{ render_function(eval_context) }}")

# Example of rendering a template with EvalContext
eval_context = {"key": "value"}
rendered_output = template.render(render_function=my_render_function, eval_context=eval_context)

print(rendered_output)
