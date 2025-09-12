from jinja2 import Environment, BaseLoader, Template

def decorated_function(function):
    def wrapper(context):
        return function(context)
    return wrapper

@decorated_function
def pass_evalcontext_to_template(context):
    return context['eval_context_key']

eval_context = {
    'eval_context_key': 'evaluation_context_value'
}

template_str = """
    The evaluation context value is: {{ pass_evalcontext_to_template(eval_context) }}
"""

environment = Environment(loader=BaseLoader)
template = environment.from_string(template_str)

result = template.render(eval_context=eval_context)

print(result)
