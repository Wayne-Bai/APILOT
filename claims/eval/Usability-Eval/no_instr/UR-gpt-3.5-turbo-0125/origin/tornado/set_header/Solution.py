
import tornado.web

class CustomHeaderHandler(tornado.web.RequestHandler):
    def set_header(self, header_name, header_value):
        self.set_header(header_name, str(header_value))

# Example Usage
# handler = CustomHeaderHandler()
# handler.set_header("Content-Type", "application/json")
