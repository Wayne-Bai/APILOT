from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop

class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello, World")

if __name__ == "__main__":
    app = Application([
        (r"/", MainHandler),
    ])
    app.listen(8888)
    print("Server is running at http://localhost:8888/")
    IOLoop.current().start()
