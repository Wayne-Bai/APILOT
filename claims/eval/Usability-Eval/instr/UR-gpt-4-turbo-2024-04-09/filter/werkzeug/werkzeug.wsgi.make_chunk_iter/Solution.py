from werkzeug import serving
from io import BytesIO

def make_chunk_iter(data, separator, limit=None, buffer_size=10240):
    """
    A generator that yields pieces of data split by a given separator.
    
    :param data: Data to be processed; can be bytes or a file-like object.
    :param separator: The separator on which the data should be split.
    :param limit: Maximum number of chunks to yield; None means unlimited.
    :param buffer_size: Size of the buffer to use for reading data.
    """
    if isinstance(data, bytes):
        data = BytesIO(data)
    
    buffer = ''
    separator = separator.decode() if isinstance(separator, bytes) else separator
    count = 0
    
    while True:
        if limit is not None and count >= limit:
            break
        
        chunk = data.read(buffer_size).decode()
        if not chunk:  # End of file/data
            if buffer:
                yield buffer
            break
        
        buffer += chunk
        while separator in buffer:
            pos = buffer.index(separator)
            yield buffer[:pos]
            buffer = buffer[pos + len(separator):]
            count += 1
            if limit is not None and count >= limit:
                break

# Example usage
data_bytes = b"Hello\nWorld\nThis\nIs\nA\nTest\nData"
for chunk in make_chunk_iter(data_bytes, b'\n'):
    print(chunk)
