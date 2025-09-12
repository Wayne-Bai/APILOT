import tornado.ioloop
import tornado.web
import tornado.wsgi
from wsgiref.simple_server import make_servers

# Define a wsgi app
def wsgi_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    return ['Hello, World!\n']

# Make the wsgi app
wsgi_app = tornado.wsgi.WSGIApplication([(r"/", tornado.web.RequestHandler),
                                        (r"/wsgi", tornado.web.RequestHandler)])

# Create an http server
container = tornado.httpserver.HTTPServer(wsgi_app)

# Start the server
if __name__ == "__main__":
    container.listen(8888)
    tornado.ioloop.IOLoop.current().start()
