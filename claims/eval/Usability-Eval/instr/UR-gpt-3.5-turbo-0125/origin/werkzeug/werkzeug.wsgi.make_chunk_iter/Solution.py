
from werkzeug.datastructures import FileStorage

def make_separator_iter(stream, separator):
    buffer = []
    for line in stream:
        if line.strip() == separator:
            yield ''.join(buffer)
            buffer = []
        else:
            buffer.append(line)
    if buffer:
        yield ''.join(buffer)

# Example usage
f = open('example.txt', 'r')
for chunk in make_separator_iter(f, '###'):
    print(chunk)
f.close()
