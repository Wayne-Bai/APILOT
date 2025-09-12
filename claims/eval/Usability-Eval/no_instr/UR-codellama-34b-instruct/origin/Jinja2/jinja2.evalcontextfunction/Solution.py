
from jinja2 import Environment, Template, Undefined, EvalContext

def evaluate(context):
    # ...
    return context.eval(context)

env = Environment()
template = env.from_string("Hello, {{ name }}!")

@evaluate
def greet(name, eval_context):
    print(f"Hello, {name}!")
