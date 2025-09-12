import tornado.ioloop
import tornado.web

class MyHandler(tornado.web.RequestHandler):
    def get(self):
        # Iterate over all cookies sent by the user
        for cookie_name in self.request.cookies.keys():
            # Expire each cookie by setting it with an expired date
            self.clear_cookie(cookie_name)
        
        self.write("All cookies have been deleted.")

def make_app():
    return tornado.web.Application([
        (r"/", MyHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server started at http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
