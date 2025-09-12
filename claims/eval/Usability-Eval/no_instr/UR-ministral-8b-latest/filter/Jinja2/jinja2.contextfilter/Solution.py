from jinja2 import Context, Env, template

def process_template(template_string, context):
    env = Env()
    template = env.from_string(template_string)
    # Assuming the context is passed as a dictionary with key-value pairs
    return template.render(context)

# Example usage:
context = {
    'name': 'Alice',
    'age': 30
}

template_string = """
    Hello {{ name }}!
    You are {{ age }} years old.
"""

result = process_template(template_string, context)
print(result)
