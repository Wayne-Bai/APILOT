from jinja2 import Environment,arda

def template_with_eval_context(eval_context, **kwargs):
    env = Environment(eval_context=eval_context)
    template_str = """
    <p>Hello {{ name }}</p>
    """
    template = env.from_string(template_str)
    return template.render(name="John")

# Example usage:
eval_context =arda()  # Use your own method of creating EvalContext
print(template_with_eval_context(eval_context))
