from jinja2 import Environment, FileSystemLoader, Template

def render_template(template_path, eval_context):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_path)
    context = {'_eval_context': eval_context}
    return template.render(context)

if __name__ == "__main__":
    eval_context = {}
    template_path = 'path/to/your/template.html'
    rendered_result = render_template(template_path, eval_context)
    print(rendered_result)
