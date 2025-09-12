from jinja2 import Environment, FileSystemLoader, contextfunction

# Define a function that will take EvalContext as the first argument
@contextfunction
def greet_user(context, username):
    eval_ctx = context.eval_ctx
    return f"Hello, {username}! (autoescape: {eval_ctx.autoescape})"

# Set up the Jinja2 environment and template loader
env = Environment(loader=FileSystemLoader('templates'))

# Register the function as a filter
env.filters['greet_user'] = greet_user

# Get the template
template = env.get_template('example_template.html')

# Render the template with a variable
output = template.render(username="Alice")

print(output)
