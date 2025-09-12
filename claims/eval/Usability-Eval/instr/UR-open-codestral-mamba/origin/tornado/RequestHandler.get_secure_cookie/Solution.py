import tornado.web

class CookieHandler(tornado.web.RequestHandler):
    def get(self):
        signed_value = self.get_argument("signed_value")
        name = self.get_argument("name")
        expires_days = self.get_argument("expires_days")
        value = self.get_signed_value(name, signed_value, expires_days=expires_days)
        if value is not None:
            self.write(signed_value)
        else:
            self.write("None")

    def validate_cookie(self):
        try:
            secret = self.settings['cookie_secret']
            name = self.get_argument("name")
            expires_days = self.get_argument("expires_days")
            value = self.get_signed_value(name, secret, expires_days=expires_days)
            return value is not None
        except:
            return False

app = tornado.web.Application([(r"/", CookieHandler)])
app.listen(8888)
tornado.ioloop.IOLoop.current().start()
