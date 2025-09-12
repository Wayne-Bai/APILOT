from werkzeug import dump_header

def dump_http_header():
    header = dump_header(
        ('Content-Type', 'text/html'),
        ('Content-Length', '1234')
    )
    print(header)
