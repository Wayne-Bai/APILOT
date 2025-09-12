import io
import werkzeug
from werkzeug.wsgi import negotiate_encoding

class SafeLineStream:
    """
    Safely iterates line-based over an input stream.

    Args:
        stream: Input stream (file-like object or bytes-like object)
        encoding: Encoding to use for decoding lines (default is 'utf-8')
    """

    def __init__(self, stream, encoding=None):
        self.stream = stream
        if encoding is None:
            encoding = negotiate_encoding(stream.read(7 if isinstance(stream, io.IOBase) else 4))
        self.encoding = encoding
        self.iterator = self.line_iterator()

    def line_iterator(self):
        while True:
            chunk = self.stream.readline()
            if not chunk and not hasattr(self.stream, 'closed') or self.stream.closed:
                break
            else:
                yield chunk.decode(self.encoding, errors='replace')

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)

    def __getitem__(self, key):
        lines = []
        for i, line in enumerate(self.iterator):
            lines.append(line)
            if i == key:
                break
        return ''.join(lines)
