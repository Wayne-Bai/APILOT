import tornado.ioloop
import tornado.web

class DeleteCookiesHandler(tornado.web.RequestHandler):
    def get(self):
        # Iterate through all cookies and clear each one
        for cookie in self.request.cookies.keys():
            self.clear_cookie(cookie)
        
        self.write("All cookies have been deleted.")

def make_app():
    return tornado.web.Application([
        (r"/delete_cookies", DeleteCookiesHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
