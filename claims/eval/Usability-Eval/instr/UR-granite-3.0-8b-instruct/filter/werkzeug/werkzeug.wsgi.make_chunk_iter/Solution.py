from werkzeug.utils import secure_filename

def make_line_iter(data, separator):
    return (line + separator for line in data.splitlines())
