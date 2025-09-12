
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # Set the header name and value
        self.set_header("Header-Name", "Header-Value")

        # Write a response
        self.write("Header set successfully!")
