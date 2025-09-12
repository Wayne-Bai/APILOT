from werkzeug.utils import LimitedStream

def safe_iterate_over_stream(input_stream, max_line_length=1024):
    stream = LimitedStream(input_stream, max_line_length)
    while True:
        line = stream.readline()
        if not line:
            break
        yield line

# Example usage:
# with open('example.txt', 'rb') as f:
#     for line in safe_iterate_over_stream(f):
#         print(line.decode('utf-8'))
