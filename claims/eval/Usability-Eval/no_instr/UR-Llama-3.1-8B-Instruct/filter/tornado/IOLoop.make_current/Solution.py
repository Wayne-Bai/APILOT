import tornado.ioloop
import tornado.web

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def main():
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()

if __name__ == "__main__":
    import sys
    sys.settrace(lambda *args: None)
    main()
