import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def set_custom_header(self, name, value):
        self.set_header(name, value)

    def get(self):
        self.set_custom_header('Content-Type', 'application/json')
        self.set_custom_header('Custom-Header', 'custom-value')
        self.write("Headers set successfully")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server started on port 8888")
    tornado.ioloop.IOLoop.current().start()
