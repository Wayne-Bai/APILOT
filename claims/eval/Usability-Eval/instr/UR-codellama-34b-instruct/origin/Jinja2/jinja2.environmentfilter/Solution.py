
from jinja2 import Environment, FileSystemLoader

def render_with_env(env):
    return env.get_template('index.html').render(environment=env)

@app.route('/')
def index():
    env = Environment(loader=FileSystemLoader('templates'))
    return render_with_env(env)
