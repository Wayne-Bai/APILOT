from jinja2 import Template

def jinja_decorator(func):
    def wrapper(*args, **kwargs):
        context = {
            'func': func,
            'args': args,
            'kwargs': kwargs
        }
        template = Template("""
            <script>
                ${func.__name__}(${args}, ${kwargs});
            </script>
        """)
        return template.render(context)
    return wrapper
