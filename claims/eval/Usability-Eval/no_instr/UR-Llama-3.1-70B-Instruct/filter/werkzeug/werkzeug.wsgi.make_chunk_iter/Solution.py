import io
from werkzeug.wsgi import LimitedStream

def make_chunk_iter(stream, separator=b'\n', limit=None, buffer_size=io.DEFAULT_BUFFER_SIZE):
    """
    Works like make_line_iter() but accepts a separator which divides chunks.
    
    :param stream: The input stream, a file descriptor or socket object.
    :param separator: The separator that divides chunks.
    :param limit: The maximum number of bytes to read.
    :param buffer_size: The size of the buffer to use for reading.
    """
    _iter = iter(LimitedStream(stream, limit=limit))
    buffer = b''

    while True:
        chunk = next(_iter, b'')
        if not chunk:
            break
        buffer += chunk
        while separator in buffer:
            nos = buffer.find(separator)
            yield buffer[:nos + len(separator)]
            buffer = buffer[nos + len(separator):]
    if buffer:
        yield buffer
