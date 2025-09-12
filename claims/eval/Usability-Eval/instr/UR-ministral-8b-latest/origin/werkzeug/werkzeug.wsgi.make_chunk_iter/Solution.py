from werkzeug.utils import imghdr, secure_filename
import werkzeug

def make_chunked_iter(data, chunk_size, separator):
    i = 0
    while i < len(data):
        yield data[i:i+chunk_size]
        i += chunk_size
        if i < len(data):
            yield separator

def make_line_iter(file_like, chunk_size, inline=True):
    separator = "\x00".encode('latin1') if inline else b""

    def on_chunk(chunk):
        if inline:
            yield chunk.decode('latin1')
        else:
            for part in chunk.decode('latin1').split(separator.decode('latin1')):
                yield b"".join(part)

    def makehydrator(func):
        def inner(X):
            if isinstance(X, werkzeug.datastructures.FileStorage):
                _, f = func(X.stream)
            else:
                f = func(X)

            if f is not None:
                for chunk in make_chunked_iter(f.read(), chunk_size, separator):
                    yield on_chunk(chunk)
        return inner
    return makehydrator

# Usage example:
file_like = werkzeug.datastructures.FileStorage(open(__file__, 'rb'))
for line in make_line_iter(file_like, 1024, inline=True):
    print(line)

