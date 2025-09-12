
import tornado.websocket

class MyWebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        print("Message received: {}".format(message))
        self.write_message("You said: {}".format(message))

    def on_close(self):
        print("WebSocket closed")

application = tornado.web.Application([
    (r'/websocket', MyWebSocketHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
