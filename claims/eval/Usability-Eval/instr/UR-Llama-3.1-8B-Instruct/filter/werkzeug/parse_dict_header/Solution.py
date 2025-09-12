from werkzeug.datastructures import Headers

class ParseHeader:
    def __init__(self, header_str):
        self.header_str = header_str
        self.headers = dict()

    def parse_header(self):
        if not isinstance(self.header_str, str):
            raise TypeError("Input should be a string")

        headers = Headers(self.header_str.splitlines())
        for key, value in headers.raw:
            self.headers[key] = value

        return self.headers

header_str = """
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Host: www.example.com
"""

parse_header = ParseHeader(header_str)
print(parse_header.parse_header())
