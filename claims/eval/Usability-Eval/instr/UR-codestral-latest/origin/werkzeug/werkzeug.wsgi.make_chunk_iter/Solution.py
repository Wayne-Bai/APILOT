from werkzeug.wsgi import ClosingIterator

def make_line_iter(stream, separator):
    """Divides an input stream into lines based on a specific separator."""
    buffer = b""
    for chunk in stream:
        buffer += chunk
        while separator in buffer:
            line, buffer = buffer.split(separator, 1)
            yield line + separator
    if buffer:
        yield buffer

def make_wsgi_app(environ, start_response):
    """WSGI Application that uses make_line_iter function."""
    input_stream = environ['wsgi.input']
    input_iter = ClosingIterator(input_stream)
    output_iter = make_line_iter(input_iter, b'\n')
    write = start_response('200 OK', [('Content-Type', 'text/plain')])
    write(b'Begin\n')
    for line in output_iter:
        # Process line
        write(line)
    write(b'End\n')
    return []
