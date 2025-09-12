from jinja2 import Environment, Template

class RenderEngine:
    def __init__(self, context, directory):
        self.context = context
        self.environ = Environment(directory=directory)

    def render(self, name):
        template = self.environ.get_template(name)
        output = template.render(evalctx=self.context)
        return output

# Example usage:
context = {'message': 'Hello, World!'}
directory = 'templates'

engine = RenderEngine(context, directory)
output = engine.render('test_template.txt')
print(output)
