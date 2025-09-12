from werkzeug.wsgi import make_chunk_iter
import io

def make_separator_line_iter(stream=None, separator=b'\n', buffer_size=8192):
    """
    Works like make_line_iter() but accepts a separator which divides chunks.
    
    :param stream: An input stream, or any object with a `read` method.
    :param separator: Separator to split the chunks. Defaults to b'\n'.
    :param buffer_size: The buffer size to read at a time.
    """
    buffer = b''
    for chunk in make_chunk_iter(stream, limit=buffer_size):
        buffer += chunk
        while separator in buffer:
            line, buffer = buffer.split(separator, 1)
            yield line
    if buffer:
        yield buffer

# Example use
if __name__ == "__main__":
    stream = io.BytesIO(b"Hello World!\nThis is a test.\nAnother line.")
    for line in make_separator_line_iter(stream):
        print(line)
