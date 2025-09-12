from jinja2 import Template

def decorate_function_with_environment(env):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(env)
        return wrapper
    return decorator

class CustomEnvironment(Template):
    def render(self, **kwargs):
        kwargs['env'] = self
        return super().render(**kwargs)

# Example usage
template_str = "{{ env.some_template_variable }}"
template = CustomEnvironment(template_str)
rendered = template.render(env={'some_template_variable': 'hello world'})
print(rendered)
