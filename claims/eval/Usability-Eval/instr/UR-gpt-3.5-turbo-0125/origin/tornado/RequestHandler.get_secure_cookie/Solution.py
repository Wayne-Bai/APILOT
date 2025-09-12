
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cookie_name = "my_cookie_name"
        signed_cookie = self.get_secure_cookie(cookie_name)
        
        if signed_cookie:
            # Validate the signed cookie here
            valid_cookie = validate_signed_cookie(signed_cookie)
            if valid_cookie:
                self.write("Valid signed cookie: {}".format(valid_cookie))
            else:
                self.write("Invalid signed cookie")
        else:
            self.write("No signed cookie found")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
