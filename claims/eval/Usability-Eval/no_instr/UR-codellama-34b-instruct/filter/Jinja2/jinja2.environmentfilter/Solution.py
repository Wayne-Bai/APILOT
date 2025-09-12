from jinja2 import Environment, select_autoescape

env = Environment(select_autoescape=True)

@env.decorator
def my_decorated_function(template, context):
    # Your function code here
    return "Hello World!"

my_decorated_function("{{ hello }}", {"hello": "World"})
