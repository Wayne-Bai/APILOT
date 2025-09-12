
from werkzeug.wsgi import LimitedStream

def iterate_lines(input_stream):
    input_stream = LimitedStream(input_stream, limit=1024)

    for line in input_stream:
        yield line

# Example of how to use iterate_lines function
input_stream = open('input.txt', 'rb')
for line in iterate_lines(input_stream):
    print(line.decode('utf-8'))
