import tornado.ioloop
import tornado.web

class Application(tornado.web.Application):
    def __init__(self):
        # Define your handlers here
        handlers = [
            (r"/", MainHandler),
        ]
        tornado.web.Application.__init__(self, handlers)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World")

# Run the IOLoop for the current thread
tornado.ioloop.IOLoop.instance().start()
