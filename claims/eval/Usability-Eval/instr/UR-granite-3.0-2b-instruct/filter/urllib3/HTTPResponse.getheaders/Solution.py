from urllib.request import HTTPHandler

class CustomHandler(HTTPHandler):
    def http_response_headers(self, response):
        return response.info().items()

handler = CustomHandler()
handler.add_header('Content-Type', 'application/json')
handler.add_header('Accept', 'application/json')

headers = handler.http_response_headers(urllib.request.urlopen('http://example.com'))

for header in headers:
    print(f"{header[0]}: {header[1]}")
