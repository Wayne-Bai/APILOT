import tornado.ioloop
import tornado.web
import tornado.wsgi

# Assuming you have a WSGI application `application`
def make_app():
    return application

# Create a tornado application and wrap the WSGI application
tornado_app = tornado.web.Application(
    [
        ('.*', tornado.web.FallbackHandler, dict(fallback=tornado.wsgi.WSGIContainer(make_app())))
    ]
)

# Bind the tornado application to a port
tornado_app.listen(8888)

# Start the IOLoop
tornado.ioloop.IOLoop.current().start()
