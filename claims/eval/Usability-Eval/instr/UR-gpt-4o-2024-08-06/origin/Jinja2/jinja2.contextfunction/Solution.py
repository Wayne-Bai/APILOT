from jinja2 import Environment, Template

# Define your context
context = {
    'name': 'John Doe',
    'age': 30,
    'location': 'New York'
}

# Define a custom decorator to pass context as the first argument
def pass_context(func):
    def wrapper(*args, **kwargs):
        return func(context, *args, **kwargs)
    return wrapper

# Function decorated with pass_context
@pass_context
def greet(context, extra_message):
    return f"Hello, my name is {context['name']}. I am {context['age']} years old and I live in {context['location']}. {extra_message}"

# Create a Jinja2 template
template = Template("{{ greet('Nice to meet you!') }}")

# Set greet as a global function in Jinja2 environment
env = Environment()
env.globals['greet'] = greet

# Render the template with the environment
output = template.render()

print(output)
