
from werkzeug import iterators

def make_chunked_line_iter(iterable, chunk_size):
    return iterators.ChunkedIterable(iterable, chunk_size)
