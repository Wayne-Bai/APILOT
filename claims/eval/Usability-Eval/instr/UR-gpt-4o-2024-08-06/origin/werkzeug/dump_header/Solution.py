from werkzeug.datastructures import Headers

def dump_http_header():
    headers = Headers()
    headers.add('Content-Type', 'text/html')
    headers.add('Content-Length', '1234')
    headers.add('Connection', 'keep-alive')

    header_str = ''
    for header in headers:
        header_str += f'{header[0]}: {header[1]}\n'
    
    return header_str

header_output = dump_http_header()
print(header_output)
