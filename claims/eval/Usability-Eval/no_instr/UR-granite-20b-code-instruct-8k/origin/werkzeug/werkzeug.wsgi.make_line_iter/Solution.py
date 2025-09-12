import werkzeug

def safely_iter_lines(input_stream):
    """
    Safely iterates line-based over an input stream.
    """
    for line in werkzeug.utils.iter_lines(input_stream):
        yield line
