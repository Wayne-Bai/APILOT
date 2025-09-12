import tornado
import tornado.web

class HttpResponse(tornado.web.HTTPServer.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)

    def set_header(self, field, value):
        """
        Sets the given response header name and value.
        All header values are converted to strings.
        """
        if field not in self._headers_written:
            self._headers['Set-Cookie'] = []
            self._headers['Cache-Control'] = []
            field = str(field).replace(' ', '-')

        value = str(value)
        self._headers.setdefault(field, []).append(value)

# Example usage:
class ExampleHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header('Content-Type', 'text/plain')
        self.set_header('Custom-Header', 'Hello, world!')
        self.write('Hello, world!')

if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/", ExampleHandler),
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
