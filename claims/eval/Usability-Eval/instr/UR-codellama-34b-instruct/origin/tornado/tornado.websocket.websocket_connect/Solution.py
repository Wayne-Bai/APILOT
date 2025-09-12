
import tornado.ioloop
import tornado.web

class EchoWebSocketHandler(tornado.websocket.WebSocketHandler):
    def on_message(self, message):
        self.write_message("You said: " + message)

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", EchoWebSocketHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
