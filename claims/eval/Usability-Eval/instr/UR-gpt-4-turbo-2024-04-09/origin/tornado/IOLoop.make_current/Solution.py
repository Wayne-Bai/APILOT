import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_ioloop_current_explicitly():
    # Create an instance of IOLoop
    loop = tornado.ioloop.IOLoop.current()
    # Explicitly set this IOLoop instance for the current thread
    tornado.ioloop.IOLoop.clear_current()
    tornado.ioloop.IOLoop.clear_instance()
    loop.make_current()

    return loop

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", MainHandler),
    ])

    loop = make_ioloop_current_explicitly()

    app.listen(8888)
    loop.start()
