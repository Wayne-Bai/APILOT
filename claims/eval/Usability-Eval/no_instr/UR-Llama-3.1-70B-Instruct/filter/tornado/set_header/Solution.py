import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')
        self.set_header('X-API-Version', 'v1')

    def get(self):
        # You can also set headers inside the get method
        self.set_header('X-Server-Time', 'Mon, 19 Apr 2021 15:45:30 GMT')
        self.write('{"message": "Hello, World!"}')

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server is up at port 8888")
    tornado.ioloop.IOLoop.current().start()
