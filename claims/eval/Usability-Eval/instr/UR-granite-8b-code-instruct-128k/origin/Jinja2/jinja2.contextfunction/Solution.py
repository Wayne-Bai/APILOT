from jinja2 import Environment, contextfilter

@contextfilter
def inject_context(ctx, value):
    ctx['injected_value'] = value
    return ''

env = Environment(extensions=[inject_context])
template = env.from_string('{{ injected_value }}')
output = template.render(inject_context=lambda: None)

print(output)  # Output: ''
