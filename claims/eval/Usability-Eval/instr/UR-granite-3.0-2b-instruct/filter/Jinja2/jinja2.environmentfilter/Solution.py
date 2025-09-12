from jinja2 import Environment, FileSystemLoader

def render_template(template_name, environment, content):
    environment.from_string(content)
    return environment.render(template_name)

env = Environment(loader=FileSystemLoader('.'))

@env.filter
def pass_env(env):
    return env

def decorated_function():
    env = {'var': 'Hello, World!'}
    return render_template('template.html', env, str(env))

if __name__ == '__main__':
    print(decorated_function())
