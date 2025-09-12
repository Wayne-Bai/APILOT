from werkzeug.utils import secure_filename

def make_line_iter_with_separator(file_like_object, separator='\n'):
    """
    Generator that yields lines from a file-like object based on a specified separator.

    :param file_like_object: A file-like object to read from.
    :param separator: The separator used to divide the chunks (default is newline '\n').
    """
    buffer = ''
    
    for chunk in iter(lambda: file_like_object.read(4096), b''):
        buffer += chunk.decode('utf-8')
        while separator in buffer:
            line, buffer = buffer.split(separator, 1)
            yield line

    if buffer:
        yield buffer
