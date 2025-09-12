import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # Set a response header. Convert value to string.
        self.set_header("X-Custom-Header", str(123))  # Example header

        # Another example, string conversion for a different data type
        self.set_header("X-Another-Header", str(3.1415))

        self.write("Headers have been set!")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
