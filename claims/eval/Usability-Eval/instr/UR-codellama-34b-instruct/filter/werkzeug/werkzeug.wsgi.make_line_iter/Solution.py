
from werkzeug import utils

def safe_iter_lines(stream):
    for line in utils.iter_lines(stream):
        yield line
