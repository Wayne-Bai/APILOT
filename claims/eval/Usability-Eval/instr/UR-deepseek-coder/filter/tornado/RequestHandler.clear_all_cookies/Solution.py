import tornado.web

class ClearCookiesHandler(tornado.web.RequestHandler):
    def get(self):
        self.clear_all_cookies()
        self.write("All cookies have been cleared.")

application = tornado.web.Application([
    (r"/clear_cookies", ClearCookiesHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
