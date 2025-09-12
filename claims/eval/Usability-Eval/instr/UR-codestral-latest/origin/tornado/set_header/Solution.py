import tornado.web

class MyHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Header-Name", "Header-Value")  # replace "Header-Name" and "Header-Value" with your desired values
