
from werkzeug.datastructures import MultiDict

def make_line_iter(text, separator='\n'):
    lines = text.split(separator)
    for line in lines:
        yield line
