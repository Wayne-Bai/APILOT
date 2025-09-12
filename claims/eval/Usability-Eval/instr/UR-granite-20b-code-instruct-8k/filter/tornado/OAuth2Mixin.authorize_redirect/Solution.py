import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # Redirect the user to obtain OAuth authorization for this service
        self.redirect("/authorize_redirect")

class OAuthHandler(tornado.web.RequestHandler):
    def get(self):
        # Start the OAuth authorization process
        self.start()

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/oauth", OAuthHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
