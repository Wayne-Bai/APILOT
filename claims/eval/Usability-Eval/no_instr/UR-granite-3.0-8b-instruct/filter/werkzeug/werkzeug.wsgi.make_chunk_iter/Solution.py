from werkzeug.utils import secure_filename

def make_line_iter(text, chunk_size, separator):
    for i in range(0, len(text), chunk_size):
        yield text[i:i + chunk_size] + separator
