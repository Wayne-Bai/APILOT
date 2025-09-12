from werkzeug.utils import iter_lines

def safely_iterate_lines(input_stream):
    for line in iter_lines(input_stream, terminate_on_eof=True):
        yield line
