import tornado.web
import tornado.wsgi
import tornado.httpserver

# Example WSGI application
def simple_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [b'Hello, world!']

# Wrap the WSGI application with Tornado's WSGIContainer
container = tornado.wsgi.WSGIContainer(simple_app)

# Create a Tornado application with the WSGI container
application = tornado.web.Application([
    (r".*", tornado.web.FallbackHandler, dict(fallback=container)),
])

# Start the Tornado HTTP server
if __name__ == "__main__":
    server = tornado.httpserver.HTTPServer(application)
    server.listen(8888)
    tornado.ioloop.IOLoop.current().start()
