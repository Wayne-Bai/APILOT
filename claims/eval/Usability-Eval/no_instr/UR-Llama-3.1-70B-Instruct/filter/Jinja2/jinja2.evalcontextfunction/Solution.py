from jinja2 import Environment, nodes
from jinja2.ext import Extension
from jinja2.parser import Parser
from jinja2BaseContext import Context

class EvalContextExtension(Extension):
    def __init__(self, environment):
        super(EvalContextExtension, self).__init__(environment)

    tags = set(['eval_context'])

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        args = [nodes.ContextReference()]

        def decorator(func):
            def wrapper(*args, **kwargs):
                return func(self.environment.eval_ctx, *args, **kwargs)

            return wrapper

        target = nodes.Name('evaluate','store', lineno=lineno)
        alias_to = nodes.ExtensionAttribute(self, 'evaluate', target, lineno=lineno)
        body = parser.parse_statements(['name:endswith', 'name:endtag'],
                                   drop_needle=True)
        return nodes.CallBlock(self.attr('_evaluate', lineno=lineno), [],
                               [], body, alias_to)

    def _evaluate(self, context, body):
        def evaluate(eval_ctx):
            return body()

        return evaluate

env = Environment(extensions=[EvalContextExtension])
context = env.context_class(lambda: {})
env.globals['evaluate'] = env.eval_ctx.call
template = env.from_string('''
{% eval_context %}
  {{ evaluate(lambda ec: "Hello " + ec.name) }}
{% end_eval_context %}
''')
print(template.render(eval_ctx={'name': 'World'}))
