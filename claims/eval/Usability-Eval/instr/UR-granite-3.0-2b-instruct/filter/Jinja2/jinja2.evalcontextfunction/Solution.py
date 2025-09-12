from jinja2 import Environment, FileSystemLoader

# Create a Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

# Define the EvalContext class
class EvalContext:
    def __init__(self, data):
        self.data = data

    def __call__(self, context, template):
        # Access the data from the EvalContext
        data = self.data
        # Use the data in the template
        template.render(data)

# Define the decorator function
def eval_context(func):
    def wrapper(context, template):
        # Create an instance of EvalContext
        ec = EvalContext(context)
        # Call the function with the EvalContext as the first argument
        return func(ec, template)
    return wrapper

# Example usage
@eval_context
def render_template(context, template):
    # Access the data from the EvalContext
    data = context.data
    # Use the data in the template
    template.render(data)
    # Return the rendered template
    return template.render()
