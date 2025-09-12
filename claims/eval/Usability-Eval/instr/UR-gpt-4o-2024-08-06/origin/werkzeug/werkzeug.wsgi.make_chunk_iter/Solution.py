from werkzeug.wsgi import ClosingIterator
from collections import deque

def custom_chunk_iter(stream, separator=b'\n'):
    """Generates chunks of data from a stream using a specified separator."""
    buffer = deque()
    chunk = b''

    for part in stream:
        chunk += part
        while separator in chunk:
            pos = chunk.index(separator)
            buffer.append(chunk[:pos])
            yield b''.join(buffer).decode()
            buffer.clear()
            chunk = chunk[pos + len(separator):]

    # Yield the leftover chunk if there is any
    if chunk:
        buffer.append(chunk)
        yield b''.join(buffer).decode()

# Example usage
# Assuming `response` is a werkzeug Response object
# with `app_iter` or any iterable stream as its body:

# with response.app_iter as stream:
#     for chunk in custom_chunk_iter(stream, separator=b'\r\n'):
#         process(chunk) # Your custom processing on each chunk
