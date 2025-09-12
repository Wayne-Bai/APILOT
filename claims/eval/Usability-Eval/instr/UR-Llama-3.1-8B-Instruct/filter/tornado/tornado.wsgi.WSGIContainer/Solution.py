# Import the Tornado library for creating the HTTP server
import tornado
from tornado.web import StaticFileHandler, Application
from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
import tornado.web

# Define a simple WSGI application
class WSGIApp(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/static/(.*)', StaticFileHandler, {'path':'static/'}),
            (r"/", SimpleWSGIApplication),
        ]
        super().__init__(handlers, autoreload = False)

class SimpleWSGIApplication(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', MainHandler),
        ]
        super().__init__(handlers, debug=True)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")

# Create an instance of WSGIApp
app = WSGIApp()
# Create a container instance from the WSGI app
container = WSGIContainer(app)
# Create an HTTP server instance
http_server = tornado.httpserver.HTTPServer(container)
# Bind to localhost on port 80
http_server.listen(80)
# Start the IOLoop
IOLoop.instance().start()
