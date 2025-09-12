from jinja2 import Environment, FileSystemLoader

# Create a Jinja2 environment
env = Environment()

# Load the template
loader = FileSystemLoader("templates")
env.loader = loader

# Define the template
template = env.get_template("my_template.j2")

# Define the EvalContext
eval_context = {"key": "value"}

# Decorate the function with @env.extend
def my_function(eval_context):
    return eval_context["key"]

# Render the template with the decorated function
output = template.render(eval_context=eval_context)

# Print the output
print(output)
