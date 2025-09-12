from tornado.web import RequestHandler
from tornado import web
import tornado.ioloop
import tornado.web.ioloop

class MyHandler(RequestHandler):
    def get(self):
        for name, value in self.cookies:
            raise web.HTTPError(500, 'Could not delete cookie')
        self.finish(('Deleted cookies',));

if __name__ == "__main__":
    app = web.application([
        (r"/", MyHandler),
    ], debug=True)
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
