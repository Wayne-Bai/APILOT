import tornado.web
from tornado.ioloop import IOLoop
from tornado.websocket import WebSocketHandler

class MyWebSocketHandler(WebSocketHandler):
    def on_message(self, message):
        # handle incoming messages from the client
        print("Received message:", message)
        self.write_message("Echo: " + message)

if __name__ == "__main__":
    app = tornado.web.Application([
        (r'/', MyWebSocketHandler),
    ])
    app.listen(8888)
    IOLoop.instance().start()
