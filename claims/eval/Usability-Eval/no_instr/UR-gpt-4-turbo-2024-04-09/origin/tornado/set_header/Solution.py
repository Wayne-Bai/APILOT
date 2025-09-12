import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # Setting a response header using set_header method
        self.set_header("Content-Type", "text/plain")
        self.write("The response header has been set.")
