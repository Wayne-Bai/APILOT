import tornado.web
import tornado.ioloop

class HeadersSettingHandler(tornado.web.RequestHandler):
    def get(self):
        # Demonstration of setting response headers
        self.set_header('Content-Type', 'text/plain')
        self.write('Hello, World!')

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", HeadersSettingHandler)
    ], default_host="localhost", cookie_secret="your_secret_key")

    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
