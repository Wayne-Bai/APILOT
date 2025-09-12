import tornado.ioloop
import tornado.web
import tornado.wsgi
from wsgiref.simple_server import make_server
from demo_app import DemoApp  # assuming you have a wsgi application defined

# Define a simple wsgi demo app
class DemoApp:
    def __call__(self, environ, start_response):
        status = '200 OK'
        headers = [('Content-type', 'text/plain')]
        start_response(status, headers)
        return ['This is a demo WSGI application']

# Method to create wsgi application
def create_wsgi_app():
    return DemoApp()

# Create WSGI application
wsgi_app = create_wsgi_app()

# Wrap the WSGI application with Tornado’s WSGI container
container = tornado.wsgi.WSGIContainer(wsgi_app)
# Create an instance of the Tornado web application
tornado_app = tornado.web.Application([(".*", tornado.wsgi.WSGIContainer, dict(wsgi_app=wsgi_app))])

# Running demo server via WSGI
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(tornado_app)
    http_server.listen(8000)
    print("Server running on port 8000")
    tornado.ioloop.IOLoop.instance().start()
