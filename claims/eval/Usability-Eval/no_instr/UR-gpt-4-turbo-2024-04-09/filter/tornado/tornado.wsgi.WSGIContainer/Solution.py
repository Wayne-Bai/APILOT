import tornado.wsgi
import tornado.httpserver
import tornado.ioloop

def wsgi_app(environ, start_response):
    """Simple WSGI application."""
    response_body = 'Hello, world!'
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    
    start_response(status, response_headers)
    return [response_body.encode('utf-8')]

if __name__ == "__main__":
    container = tornado.wsgi.WSGIContainer(wsgi_app)
    http_server = tornado.httpserver.HTTPServer(container)
    http_server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
