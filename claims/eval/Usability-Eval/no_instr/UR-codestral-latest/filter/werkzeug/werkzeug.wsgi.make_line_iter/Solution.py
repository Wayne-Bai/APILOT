from werkzeug.wsgi import wrap_file

def iter_lines(input_stream):
    for line in wrap_file(input_stream, buffer_size=1024).readlines():
        yield line.decode('utf-8')
