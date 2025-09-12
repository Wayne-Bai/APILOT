from werkzeug.exceptions import RequestMovedPermanently

class QuoteHeaderMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        if 'HTTP_HOST' in environ and environ['HTTP_HOST'].endswith('.com'):
            quote_host_value = environ['HTTP_HOST'].encode('isascii','replace')
            for i in range(len(quote_host_value)):
                if not 32 <= quote_host_value[i] <= 126 or quote_host_value[i] in ("/", "\\", ":", "?", "#"):
                    quote_host_value = quote_host_value[:i] + '.' + quote_host_value[i+1:]
            environ['HTTP_HOST'] = quote_host_value.decode('utf-8')
        return self.app(environ, lambda status: start_response(status, []))

# Example usage:
from wsgi import app

quote_header_middleware = QuoteHeaderMiddleware(app)
