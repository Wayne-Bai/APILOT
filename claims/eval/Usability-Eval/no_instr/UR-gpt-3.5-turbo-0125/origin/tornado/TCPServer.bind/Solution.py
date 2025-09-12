
import tornado.ioloop
import tornado.httpserver
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, Tornado!")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    port = 8888
    address = "localhost"
    
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(port, address)

    tornado.ioloop.IOLoop.current().start()
