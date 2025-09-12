from werkzeug import Request, QuotedHeader

def quote_header(header, value):
    return QuotedHeader(header, quote=True).add(header, value)

# Example usage:
request = Request('GET', 'https://example.com')
quoted_header = quote_header('My-Header', 'My Value')
print(quoted_header.get(quote=True))
