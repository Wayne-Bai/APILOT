from jinja2 import contextfunction

@contextfunction
def my_function(context):
    # Accessing context variables
    var1 = context.get('var1')
    var2 = context.get('var2')

    # Your code logic here

    return result
