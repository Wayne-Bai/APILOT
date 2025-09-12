from jinja2 import Environment, Template

def decorated_function(template, ctx):
    return template.render(ctx)

env = Environment()
template = env.from_string("""
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
</body>
</html>
""")

ctx = {
    'title': 'Sample Page',
    'name': 'John Doe'
}

rendered_template = decorated_function(template, ctx)
print(rendered_template)
