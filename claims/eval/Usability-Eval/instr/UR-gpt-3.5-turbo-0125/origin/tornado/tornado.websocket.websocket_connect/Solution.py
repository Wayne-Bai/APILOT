
import tornado.websocket
import tornado.ioloop

class MyWebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket connection opened")

    def on_message(self, message):
        print(f"Message received: {message}")
        self.write_message(f"Echoing back: {message}")

    def on_close(self):
        print("WebSocket connection closed")

def make_app():
    return tornado.web.Application([
        (r"/", MyWebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
