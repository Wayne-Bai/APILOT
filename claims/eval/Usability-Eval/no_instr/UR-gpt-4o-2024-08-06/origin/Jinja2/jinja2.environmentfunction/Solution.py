from jinja2 import Environment, Template, contextfunction

# A custom function that prints a message, showcasing access to the environment
@contextfunction
def custom_greeting(context, name):
    env = context.environment  # Accessing the environment from the context
    return f"Hello, {name}! You are using {env}."

# Initialize the Jinja2 environment
env = Environment()

# Register the custom function in the environment
env.globals['custom_greeting'] = custom_greeting

# Template string that uses the custom function
template_string = "Custom greeting: {{ custom_greeting('Alice') }}"

# Create a Template instance with the template string
template = env.from_string(template_string)

# Render the template
output = template.render()

print(output)
