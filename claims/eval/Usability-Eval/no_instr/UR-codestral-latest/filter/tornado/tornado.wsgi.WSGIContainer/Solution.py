import tornado.ioloop
import tornado.web
import tornado.wsgi
from your_wsgi_app import application  # replace with your WSGI app

def main():
    container = tornado.wsgi.WSGIContainer(application)
    http_server = tornado.httpserver.HTTPServer(container)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
