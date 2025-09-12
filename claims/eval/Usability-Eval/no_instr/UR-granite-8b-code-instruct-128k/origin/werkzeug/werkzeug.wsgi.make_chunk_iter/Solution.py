from werkzeug.wsgi import make_line_iter

def make_chunk_iter(environ, separator=b'\n'):
    """Generator that yields chunks from the request body."""
    iter = make_line_iter(environ)
    while True:
        line = next(iter, None)
        if line is None:
            break
        yield line + separator
