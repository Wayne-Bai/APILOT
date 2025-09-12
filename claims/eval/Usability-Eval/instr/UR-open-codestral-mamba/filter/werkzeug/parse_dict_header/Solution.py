from werkzeug.datastructures import Headers

def parse_headers(header_list):
    headers = Headers(header_list)
    return dict(headers)

# Example usage
header_list = [
    ('Content-Type', 'text/html'),
    ('Content-Length', '1024'),
    ('Cache-Control', 'no-cache'),
]

print(parse_headers(header_list))  # Output: {'Content-Type': 'text/html', 'Content-Length': '1024', 'Cache-Control': 'no-cache'}
