from werkzeug import caching
from werkzeug import exceptions

sections = [
    (('Accept-Ranges', 'bytes'),
     ('Connection', 'keep-alive'),
     ('Content-Length', '2738'),
     ('Content-Type', 'text/plain'))
]
headers = {key: value for key, value in sections}

print(headers)
