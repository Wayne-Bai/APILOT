# Import the Template class from the templating module in Werkzeug
from werkzeug.template import Template

# Define a string template with placeholders
template_str = """
Hello, {{ username }}!
You are {{ age }} years old.
"""

# Create a Template object
template = Template(template_str)

# Data for the placeholders
data = {'username': 'John', 'age': 30}

# Render the template with the given data
rendered_str = template.render(data)

# Print the rendered string
print(rendered_str)

# Output:
# Hello, John!
# You are 30 years old.
