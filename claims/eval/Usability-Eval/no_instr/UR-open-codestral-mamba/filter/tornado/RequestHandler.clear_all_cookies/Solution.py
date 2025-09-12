import tornado.web
import tornado.ioloop

class DeleteCookiesHandler(tornado.web.RequestHandler):
    def get(self):
        self.clear_all_cookies()
        self.write("All cookies have been deleted.")

def make_app():
    return tornado.web.Application([
        (r"/delete_cookies", DeleteCookiesHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
