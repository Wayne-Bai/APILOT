import tornado.wsgi
import tornado.httpserver
import tornado.ioloop
from your_application import your_application

application = tornado.wsgi.WSGIContainer(your_application())
http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(8000)
tornado.ioloop.IOLoop.instance().start()
