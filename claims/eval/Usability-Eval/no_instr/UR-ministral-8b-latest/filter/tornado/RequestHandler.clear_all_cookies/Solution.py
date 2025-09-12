import tornado.ioloop
import tornado.web

class RemoveCookiesHandler(tornado.web.RequestHandler):
    def get(self):
        response = tornado.web.Response()
        # Ensure all incoming cookies are deleted
        for key in self.request.headers.get('Cookie', '').split(';'):
            self.request.set_cookie(key.strip(), '', expires=0)
        self.write('Cookies removed')

def make_app():
    return tornado.web.Application([
        (r"/remove-cookies", RemoveCookiesHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
