
import tornado.wsgi
import tornado.httpserver
import tornado.ioloop
import wsgiref.simple_server

def wsgi_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [b"Hello, World!"]

if __name__ == '__main__':
    container = tornado.wsgi.WSGIContainer(wsgi_app)
    http_server = wsgiref.simple_server.make_server('', 8888, container)
    http_server.serve_forever()
