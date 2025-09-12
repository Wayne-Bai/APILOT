from werkzeug.datastructures import FileStorage

def make_chunk_iter(file, chunk_size=1024):
    return FileStorage(file).make_line_iter(chunk_size)
