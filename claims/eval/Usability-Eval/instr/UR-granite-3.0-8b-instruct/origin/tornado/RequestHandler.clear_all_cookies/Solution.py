import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        # Attempt to delete all the cookies the user sent with this request.
        for cookie_name in self.request.cookies.keys():
            self.delete_cookie(cookie_name)

        self.write("All cookies deleted.")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
