
from werkzeug.utils import cached_property

def format_string(string: str, **kwargs) -> str:
    """Formats a string using the String-Template syntax."""
    template = cached_property(lambda: string[1:-1])
    return template.format(**kwargs)
