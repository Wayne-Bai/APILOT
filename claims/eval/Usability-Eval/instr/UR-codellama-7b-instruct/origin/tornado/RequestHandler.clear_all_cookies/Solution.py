
import tornado.web

class DeleteCookiesHandler(tornado.web.RequestHandler):
    def get(self):
        self.clear_cookie("key")
        self.clear_cookie("another-key")
        self.write({"message": "Cookies deleted successfully!"})
