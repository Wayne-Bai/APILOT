from jinja2 import Environment, FileSystemLoader, MetaData

# Create an environment for Jinja2 templates
env = Environment(loader=FileSystemLoader('templates'), metadata=MetaData())

def decorator(func):
    def wrapper(eval_context, *args, **kwargs):
        # Call the original function with the eval_context as the first argument
        return func(eval_context, *args, **kwargs)
    return wrapper

def example_function(eval_context):
    return f"Hello from {eval_context}!"

# Example usage
if __name__ == "__main__":
    eval_context = {"name": "Alice"}

    # Render a template using the eval_context
    with env.get_template('template.jinja') as template:
        rendered_template = template.render(eval_context=eval_context)
        print(rendered_template)
