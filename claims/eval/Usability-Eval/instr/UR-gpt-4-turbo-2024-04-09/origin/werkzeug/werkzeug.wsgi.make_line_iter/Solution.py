from werkzeug.wsgi import wrap_file

def safe_line_iterator(input_stream):
    """ Safely iterates line-by-line over an input stream. """
    wrapped_stream = wrap_file(input_stream)
    for line in wrapped_stream:
        yield line.decode('utf-8').strip()
