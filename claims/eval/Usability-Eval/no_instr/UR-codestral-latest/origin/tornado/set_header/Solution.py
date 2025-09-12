import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        header_name = "Example-Header"
        header_value = "Example-Value"
        self.set_header(header_name, header_value)
        self.write("Headers have been set.")
