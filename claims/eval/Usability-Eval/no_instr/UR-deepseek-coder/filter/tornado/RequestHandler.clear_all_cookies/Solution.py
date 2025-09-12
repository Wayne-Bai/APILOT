import tornado.web

class DeleteCookiesHandler(tornado.web.RequestHandler):
    def get(self):
        # Delete all cookies sent by the user
        for cookie_name in self.request.cookies:
            self.clear_cookie(cookie_name)
        self.write("All cookies have been deleted.")

application = tornado.web.Application([
    (r"/delete_cookies", DeleteCookiesHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
