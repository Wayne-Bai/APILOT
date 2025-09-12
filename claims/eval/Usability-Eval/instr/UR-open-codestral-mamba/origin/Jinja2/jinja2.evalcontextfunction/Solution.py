from jinja2 import Environment, FunctionLoader, select_autoescape

def eval_context(environment, context):
    def context_function(name, context_obj, context):
        return context_obj[name](context)
    environment.globals['context'] = context
    environment.globals.update(context)

# Define your environment and autoescape
env = Environment(loader=FunctionLoader(lambda x: x), autoescape=select_autoescape(['html', 'xml']))

# Define your template
template_string = "Hello {{ context.name }}!"

# Define your context or data
context = {"name": "Jinja2"}

# Call the eval_context function before rendering the template
eval_context(env, context)

# Finally render the template
output = env.from_string(template_string).render()

print(output)
