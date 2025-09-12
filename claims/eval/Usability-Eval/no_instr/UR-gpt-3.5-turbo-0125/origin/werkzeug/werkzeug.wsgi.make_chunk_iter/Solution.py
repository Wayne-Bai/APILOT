
from werkzeug._compat import BytesIO

def make_line_iter_with_separator(data, separator):
    buf = BytesIO(data)
    buf.seek(0)
    line = []
    for char in buf.read(1):
        if char == separator:
            yield b''.join(line)
            line = []
        else:
            line.append(char)
    if line:
        yield b''.join(line)

# Usage
data = b'Hello|World|Python|Programming'
separator = b'|'
for line in make_line_iter_with_separator(data, separator):
    print(line.decode('utf-8'))
