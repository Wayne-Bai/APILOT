import tornado.ioloop
import tornado.web
from tornado.wsgi import WSGIContainer
from werkzeug.wrappers import Request, Response

# A simple WSGI application
def simple_app(environ, start_response):
    request = Request(environ)
    response = Response('Hello, WSGI world!', mimetype='text/plain')
    return response(environ, start_response)

# Create a Tornado application and mount the WSGI app
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Welcome to the Tornado WSGI application!")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    wsgi_app = WSGIContainer(simple_app)
    app.mount("/wsgi", wsgi_app)  # Mount the WSGI app under /wsgi

    app.listen(8888)
    print("Tornado server started at http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
