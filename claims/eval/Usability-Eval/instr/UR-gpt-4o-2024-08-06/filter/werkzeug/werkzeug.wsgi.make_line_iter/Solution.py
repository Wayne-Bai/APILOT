from werkzeug.wsgi import LimitedStream

def safely_iterate_lines(input_stream, buffer_size=1024):
    limited_stream = LimitedStream(input_stream, buffer_size)
    
    for line in limited_stream:
        yield line.decode('utf-8')

# Example usage:
# with open('somefile.txt', 'rb') as f:
#     for line in safely_iterate_lines(f):
#         print(line)
