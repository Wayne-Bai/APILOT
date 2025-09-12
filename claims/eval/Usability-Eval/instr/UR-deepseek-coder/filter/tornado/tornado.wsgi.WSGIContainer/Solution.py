import tornado.httpserver
import tornado.ioloop
import tornado.wsgi

# Example WSGI application (replace this with your actual WSGI app)
def simple_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [b'Hello, world!']

# Wrap the WSGI application with Tornado's WSGIContainer
container = tornado.wsgi.WSGIContainer(simple_app)

# Create a Tornado HTTP server
http_server = tornado.httpserver.HTTPServer(container)

# Bind the server to a port
http_server.listen(8888)

# Start the Tornado IOLoop
tornado.ioloop.IOLoop.current().start()
