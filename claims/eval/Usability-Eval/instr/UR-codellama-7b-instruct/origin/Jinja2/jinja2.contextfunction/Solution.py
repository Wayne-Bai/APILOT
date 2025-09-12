
from jinja2 import Template
from decorators.cached import pass_context

@pass_context(1)
def my_function():
    return "This is my function"

template = Template("{{my_function()}}")
output = template.render(my_function=my_function)
print(output) # This is my function
