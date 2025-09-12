import tornado.ioloop
import tornado.web
import tornado.websocket

class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def on_message(self, message):
        self.write_message(message)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write_body("<html><body><script src='/static/echo.js'></script></body></html>")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/ws", EchoWebSocket),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
