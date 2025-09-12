import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # Get the signed cookie from the request
        signed_cookie = self.get_secure_cookie("my_cookie")

        # Check if the signed cookie is valid
        if signed_cookie:
            self.write("Signed cookie value: " + signed_cookie.decode("utf-8"))
        else:
            self.write("Signed cookie not found or invalid")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
