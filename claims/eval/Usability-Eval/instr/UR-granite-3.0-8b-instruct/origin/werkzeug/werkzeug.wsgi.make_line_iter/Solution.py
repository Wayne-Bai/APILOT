from werkzeug.utils import iter_lines

def safe_iterate_lines(input_stream):
    for line in iter_lines(input_stream, newline=None):
        yield line
