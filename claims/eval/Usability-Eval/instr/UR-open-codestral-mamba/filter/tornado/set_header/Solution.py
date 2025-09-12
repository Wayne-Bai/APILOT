import tornado.web

class SetHeaderHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("HeaderName", "HeaderValue")

# Assume we have an application object
application = tornado.web.Application([
    (r"/", SetHeaderHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
