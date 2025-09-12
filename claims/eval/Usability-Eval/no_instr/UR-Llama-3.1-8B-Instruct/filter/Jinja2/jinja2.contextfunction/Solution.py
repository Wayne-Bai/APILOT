from jinja2 import Template, Environment, meta

# Render template with passed context
class PassContext:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        context = kwargs['context']
        return self.func(*args, environment=kwargs['environment'], context=context)

environment = Environment(extensions=['jinja2.ext.do', 'jinja2.ext.loopcontrols'])

# Example usage
template = Template('Hello {{ context.name }}')

@PassContext
def render_template(template_str, context, environment):
    return template.render(context)

context = {'name': 'John'}
result = render_template(template_str=template, context=context, environment=environment)
print(result)
