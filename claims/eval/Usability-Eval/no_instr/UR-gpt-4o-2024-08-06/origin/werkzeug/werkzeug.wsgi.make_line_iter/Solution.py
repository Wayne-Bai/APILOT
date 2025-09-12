from werkzeug.wsgi import LimitedStream

def safely_read_lines(input_stream, max_content_length):
    """
    Safely reads lines from an input stream with a maximum content length limit.

    :param input_stream: A file-like object to read from.
    :param max_content_length: Maximum number of bytes to read.
    :return: A generator yielding lines from the input stream.
    """
    limited_stream = LimitedStream(input_stream, max_content_length)

    while True:
        line = limited_stream.readline()
        if not line:  # End of stream
            break
        yield line.decode('utf-8')  # Assuming the stream is UTF-8 encoded

# Example usage:
# with open('some_file.txt', 'rb') as f:
#     for line in safely_read_lines(f, max_content_length=1024):
#         print(line)
