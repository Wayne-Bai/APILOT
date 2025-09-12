
from werkzeug.utils import format_string

template = "Hello {{ name }}, your age is {{ age }}"
context = {"name": "Alice", "age": 30}

formatted_string = format_string(template, **context)
print(formatted_string)
