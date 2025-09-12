from jinja2 import Environment, FunctionLoader, select_autoescape

# Mock template data
my_data = {
    'key1': 'value1',
    'key2': 'value2'
}

def load_template(template_name):
    if template_name == 'template1.html':
        from markupsafe import escape
        return f'This is a template: {escape(my_data["key1"])}'
    else:
        return None

env = Environment(loader=FunctionLoader(load_template), autoescape=select_autoescape())
template = env.get_template('template1.html')
output = template.render(EvalContext=my_data)
print(output)
