from werkzeug.utils import escape

def template_format(template, **context):
    """
    A simple String-template engine using format strings.

    :param template: The template string to render.
    :param context: Mapping of template variable names to values.
    """
    def missing(key):
        raise KeyError(key)

    return template.format_map(_TemplateMapping(context, missing))


class _TemplateMapping:
    """A simple string-key mapping for format strings."""

    def __init__(self, data, default):
        self.data = data
        self.default = default

    def __getitem__(self, key):
        try:
            return self.data[key]
        except KeyError:
            return self.default(key)

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)


# Example usage:
template_string = "Hello, {name}! You are {age} years old."
context = {"name": "John", "age": 30}

formatted_string = template_format(template_string, **context)
print(escape(formatted_string))  # Using escape to prevent XSS attacks
