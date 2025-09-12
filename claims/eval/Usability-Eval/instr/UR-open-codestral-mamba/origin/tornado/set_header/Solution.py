import tornado.web

class MyHandler(tornado.web.RequestHandler):
    def set_custom_header(self, name, value):
        self.set_header(name, str(value))

# Usage
handler = MyHandler()
handler.set_custom_header("Content-Type", "application/json")
