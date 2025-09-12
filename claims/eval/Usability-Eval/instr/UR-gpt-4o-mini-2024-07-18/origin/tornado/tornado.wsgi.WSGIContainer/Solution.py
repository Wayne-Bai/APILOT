
import tornado.ioloop
import tornado.web
from tornado.wsgi import WSGIAdapter

def make_wsgi_app():
    from wsgiref.simple_server import make_server

    # Here you can define your WSGI application
    def simple_wsgi_app(environ, start_response):
        status = '200 OK'
        headers = [('Content-Type', 'text/plain')]
        start_response(status, headers)
        return [b"Hello World from WSGI app"]

    return simple_wsgi_app

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World from Tornado!")

def make_tornado_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    # Create Tornado application
    tornado_app = make_tornado_app()
    
    # Wrap WSGI application to be compatible with Tornado
    wsgi_app = make_wsgi_app()
    wsgi_adapter = WSGIAdapter(wsgi_app)
    
    # Add WSGI route to Tornado application
    tornado_app.add_handlers(r'.*$', [
        (r'/wsgi', wsgi_adapter),
    ])

    # Start the Tornado server
    tornado_app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
