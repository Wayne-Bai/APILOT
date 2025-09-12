from jinja2 import Environment, evalcontext, Template
import os

# Define the environment and evaluation context
env = Environment()
eval_ctx = evalcontext.EvalContext(env)

# Define the template as a string
template_str = "{% if some_var %}Hello, {{ name }}!{% endif %}"

# Compile the template
template = Template(template_str)

# Render the template with the evaluation context
result = template.render({"some_var": True, "name": "John Doe"}, eval_ctx=eval_ctx)

print(result)
