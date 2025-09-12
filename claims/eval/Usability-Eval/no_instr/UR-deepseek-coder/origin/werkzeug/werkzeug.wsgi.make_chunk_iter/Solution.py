from werkzeug.utils import cached_property

class LineIterator:
    def __init__(self, data, separator='\n'):
        self.data = data
        self.separator = separator
        self.index = 0

    @cached_property
    def chunks(self):
        return self.data.split(self.separator)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.chunks):
            raise StopIteration
        chunk = self.chunks[self.index]
        self.index += 1
        return chunk

# Example usage:
# data = "line1\nline2\nline3"
# iterator = LineIterator(data)
# for line in iterator:
#     print(line)
