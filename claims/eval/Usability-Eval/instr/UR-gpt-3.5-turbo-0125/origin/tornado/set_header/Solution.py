
import tornado.web

class CustomHeaderHandler(tornado.web.RequestHandler):
    def set_header(self, name, value):
        self.clear_header(name)
        converted_value = str(value)
        self.set_header(name, converted_value)

# Usage
app = tornado.web.Application([
    (r"/set_header", CustomHeaderHandler),
])

if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
