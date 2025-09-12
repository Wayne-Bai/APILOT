import jinja2

def pass_eval_context(f):
    """Decorator to pass the EvalContext to the function."""
    def wrapper(eval_context, *args, **kwargs):
        return f(eval_context, *args, **kwargs)
    return jinja2.contextfunction(wrapper)

@pass_eval_context
def get_context_info(eval_context):
    """Function to use the passed EvalContext."""
    return f"Current template: {eval_context.name}"

# Set up Jinja2 environment
env = jinja2.Environment(loader=jinja2.DictLoader({'my_template': "{{ get_context_info() }}"}))

# Render template
template = env.get_template('my_template')
rendered_template = template.render()
print(rendered_template)
