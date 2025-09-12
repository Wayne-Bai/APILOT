from werkzeug.utils import secure_filename

def make_line_iter_with_separator(file, separator):
    """Yield lines from a file split by a given separator."""
    buffer = ""
    while True:
        chunk = file.read(1024)  # Read in chunks
        if not chunk:
            if buffer:
                yield buffer
            break
        buffer += chunk
        lines = buffer.split(separator)
        *complete_lines, buffer = lines
        for line in complete_lines:
            yield line
