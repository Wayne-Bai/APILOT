from jinja2 import Environment, FileSystemLoader, select_autoescape

def custom_decorator(func):
    def wrapper(*args, **kwargs):
        # Do something before executing the function
        # Here we are just printing a message
        print("Before executing the function")
        result = func(*args, **kwargs)
        # Do something after executing the function
        # Here we are just printing a message
        print("After executing the function")
        return result
    return wrapper

# This is our template render function
@custom_decorator
def render_template(context):
    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')
    output = template.render(context)
    print(output)

# We need to call the render_template function and pass the context
render_template({'name': 'John Doe'})
