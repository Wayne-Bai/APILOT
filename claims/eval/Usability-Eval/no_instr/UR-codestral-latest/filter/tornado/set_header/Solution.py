import tornado.web

class MyHandler(tornado.web.RequestHandler):
    def get(self):
        header_name = "your_header_name"
        header_value = "your_header_value"
        self.set_header(header_name, header_value)
