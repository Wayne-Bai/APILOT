
import tornado.web
import tornado.httpserver
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.bind(8000, address="localhost")
    http_server.serve_forever()
