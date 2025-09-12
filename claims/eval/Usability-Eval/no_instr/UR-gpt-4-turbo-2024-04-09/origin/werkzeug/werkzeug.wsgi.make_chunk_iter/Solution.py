from werkzeug.wsgi import LimitedStream

def make_chunk_iter(stream, separator, limit=None, buffer_size=10*1024):
    """
    Generator that yields chunks of data from a stream divided by a specific separator.
    :param stream: an input stream (file-like object)
    :param separator: a string that defines the end of a chunk
    :param limit: maximum bytes to read from the stream
    :param buffer_size: size of buffer to use when reading
    """
    if not isinstance(stream, LimitedStream):
        stream = LimitedStream(stream, limit)
    
    leftover = b''
    while True:
        buffer = stream.read(buffer_size)
        if not buffer:
            if leftover:
                yield leftover
            break
        
        chunks = buffer.split(separator)
        if len(chunks) > 1:
            yield leftover + chunks[0]
            for chunk in chunks[1:-1]:
                yield chunk
            leftover = chunks[-1]
        else:
            leftover += chunks[0]
    if leftover:
        yield leftover
