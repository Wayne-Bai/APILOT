from werkzeug.wrappers import Response

response = Response()
response.data = [b'Hello, ', b'world!']
response.headers['Content-Length'] = str(sum(len(chunk) for chunk in response.data))
if 'ETag' not in response.headers:
    response.set_etag()
