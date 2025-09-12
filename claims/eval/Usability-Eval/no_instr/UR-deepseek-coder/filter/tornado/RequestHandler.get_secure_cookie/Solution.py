import tornado.web
import tornado.escape

class CookieHandler(tornado.web.RequestHandler):
    def get(self):
        cookie_name = "my_signed_cookie"
        secret = "my_secret_key"
        signed_value = self.get_cookie(cookie_name)
        
        if signed_value:
            try:
                value = tornado.escape.url_unescape(signed_value)
                # Validate the signed cookie
                if tornado.web.create_signed_value(secret, cookie_name, value) == signed_value:
                    self.write(f"Valid signed cookie: {value}")
                else:
                    self.write("Invalid signed cookie")
            except Exception as e:
                self.write(f"Error validating cookie: {e}")
        else:
            self.write("No signed cookie found")

def make_app():
    return tornado.web.Application([
        (r"/cookie", CookieHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
