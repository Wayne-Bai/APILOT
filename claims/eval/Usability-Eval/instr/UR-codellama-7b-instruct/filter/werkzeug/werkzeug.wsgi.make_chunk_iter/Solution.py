
from werkzeug import iter_chunked

def make_line_iter(separator):
    return iter_chunked(lambda chunk: chunk.split(separator), '\\n')
