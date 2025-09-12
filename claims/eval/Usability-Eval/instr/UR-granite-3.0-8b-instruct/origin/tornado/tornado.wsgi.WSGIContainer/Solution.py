import tornado.wsgi
import tornado.httpserver
import tornado.ioloop

def make_wsgi_app():
    # Replace this with your actual WSGI application
    def wsgi_app(environ, start_response):
        status = '200 OK'
        headers = [('Content-type', 'text/plain')]
        start_response(status, headers)
        return [b'Hello, World!']

    return wsgi_app

if __name__ == '__main__':
    app = make_wsgi_app()
    server = tornado.httpserver.HTTPServer(tornado.wsgi.WSGIContainer(app))
    server.listen(8888)
    tornado.ioloop.IOLoop.current().start()
