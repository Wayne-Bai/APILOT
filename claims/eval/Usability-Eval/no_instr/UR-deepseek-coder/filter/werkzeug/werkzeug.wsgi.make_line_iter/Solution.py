from werkzeug.utils import LimitedStream

def safe_iter_lines(input_stream, buffer_size=1024):
    stream = LimitedStream(input_stream, buffer_size)
    pending = b''

    while True:
        chunk = stream.read(buffer_size)
        if not chunk:
            break

        lines = (pending + chunk).splitlines(True)
        for line in lines[:-1]:
            yield line.rstrip(b'\r\n')

        pending = lines[-1]

    if pending:
        yield pending.rstrip(b'\r\n')

# Example usage:
# with open('example.txt', 'rb') as f:
#     for line in safe_iter_lines(f):
#         print(line.decode('utf-8'))
