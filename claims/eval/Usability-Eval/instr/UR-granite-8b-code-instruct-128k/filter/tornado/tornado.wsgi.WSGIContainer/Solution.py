import tornado
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
 
class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello, World!")
 
if __name__ == "__main__":
    app = Application([
        (r"/", MainHandler),
    ])
    app.listen(8000)
    IOLoop.instance().start()