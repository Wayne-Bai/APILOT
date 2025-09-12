from werkzeug.utils import escape

def string_template_formatter(template, **kwargs):
    escaped_kwargs = {k: escape(v) for k, v in kwargs.items()}
    return template.format(**escaped_kwargs)

template = "Hello, {name}! You have {messages} new messages."
formatted_string = string_template_formatter(template, name="John", messages=5)
print(formatted_string)
