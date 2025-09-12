import tornado.wsgi
import tornado.httpserver
import tornado.ioloop
import wsgiref.simple_server

# Create a simple WSGI application
def simple_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)
    return [b"Hello from WSGI application!"]

# Convert the WSGI application to a Tornado WSGI container
wsgi_container = tornado.wsgi.WSGIContainer(simple_app)

# Create an HTTP server with the WSGI container as the request handler
http_server = tornado.httpserver.HTTPServer(wsgi_container)

# Bind the server to port 8888
http_server.listen(8888)

# Start the Tornado IOLoop to handle requests
print("Serving on http://localhost:8888")
tornado.ioloop.IOLoop.current().start()
