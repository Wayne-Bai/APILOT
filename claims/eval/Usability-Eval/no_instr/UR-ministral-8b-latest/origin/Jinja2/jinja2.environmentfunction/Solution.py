from jinja2 import Environment, FileSystemLoader

# Create an environment and load the templates from the directory
env = Environment(loader=FileSystemLoader('.'))

def render_template(template_name, **context):
    """
    Render a Jinja2 template with the given context and return the result.
    """
    template = env.get_template(template_name)
    return template.render(context)

# Example usage
if __name__ == "__main__":
    render_template('template.html', some_variable='Some value')
