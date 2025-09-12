from jinja2 import Template

def my_function(context):
    # Do something with the context
    print("Hello, world!")

template = Template('my_function')
decorator = template.get_attribute('decors')
decorated_function = decorator(my_function)

context = {'name': 'Jane', 'age': 30}
result = decorated_function(context)
print(result)
