
from werkzeug.utils import cached_property
from io import StringIO

class MyStringIterator:
    def __init__(self, string, separator='\n'):
        self.string = string
        self.separator = separator

    @cached_property
    def line_iterator(self):
        return iter(StringIO(self.string).readlines(), self.separator)
