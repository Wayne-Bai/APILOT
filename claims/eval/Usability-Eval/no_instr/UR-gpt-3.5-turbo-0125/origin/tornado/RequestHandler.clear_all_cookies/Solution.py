
import tornado.web

class DeleteCookiesHandler(tornado.web.RequestHandler):
    def get(self):
        self.clear_all_cookies()
        self.write("All cookies have been deleted.")

app = tornado.web.Application([
    (r"/delete_cookies", DeleteCookiesHandler),
])

if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
