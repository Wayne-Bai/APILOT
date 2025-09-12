
import tornado.web

class CookieHandler(tornado.web.RequestHandler):
    def validate_cookie(self, cookie):
        # Here you can use any validation method you prefer,
        # this is a placeholder
        return True

    def get(self):
        cookie = self.get_cookie("mycookie")

        if cookie and self.validate_cookie(cookie):
            self.write({"cookie": cookie})
        else:
            self.write(None)

