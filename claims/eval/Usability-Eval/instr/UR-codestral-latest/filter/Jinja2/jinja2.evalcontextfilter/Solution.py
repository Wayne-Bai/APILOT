from jinja2 import Environment, nodes
from jinja2.ext import Extension

class PassEvalContextExtension(Extension):
    def __init__(self, environment):
        super(PassEvalContextExtension, self).__init__(environment)
        self.environment.extend(
            node_class_callback=self.node_class_callback
        )

    def node_class_callback(self, node_class, node_args):
        if node_class == nodes.Call:
            node_args.append(nodes.Name('ctx', 'load'))
        return node_class

def my_decorator(func):
    def wrapper(eval_context, *args, **kwargs):
        return func(eval_context, *args, **kwargs)
    return wrapper

env = Environment(extensions=[PassEvalContextExtension])

@env.filter
@my_decorator
def my_filter(eval_context, value):
    # Your code here
    pass
