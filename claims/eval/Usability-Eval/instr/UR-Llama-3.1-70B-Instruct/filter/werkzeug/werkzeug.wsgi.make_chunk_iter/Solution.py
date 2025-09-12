from werkzeug.utils import iterate_chunks

def make_separator_iter(stream, separator, limit=None):
    """
    Reads chunks from a stream until a specified separator is found.
    
    Args:
        stream: Input stream. This can be another wsgi input stream.
        separator: The separator to be searched in the stream.
        limit: The maximum amount of data to be read from the stream.
        
    Yields:
        Chunks from the stream.
    """
    separator_len = len(separator)
    buf = b''

    for chunk in iterate_chunks(stream, limit=limit):
        buf += chunk
        idx = buf.find(separator)
        while idx!= -1:
            yield buf[:idx]
            buf = buf[idx + separator_len:]
            idx = buf.find(separator)
    if buf:
        yield buf

# Example usage:
if __name__ == "__main__":
    # Create a sample stream
    class SampleStream:
        def __init__(self, data):
            self.data = data

        def read(self, limit=None):
            return self.data[:limit]

        def close(self):
            pass

    # Create a sample stream with some data
    stream = SampleStream(b"This is a sample data. This data should be divided into chunks by the '.' separator.")

    # Call make_separator_iter() function with sample strea and '.' separator
    for chunk in make_separator_iter(stream, b'.'):
        print(chunk.decode('utf-8'))
