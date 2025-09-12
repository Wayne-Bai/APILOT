
import tornado.web

class handler(tornado.web.RequestHandler):
    def get(self):
        self.clear_cookies()
        self.write("All cookies have been deleted.")
