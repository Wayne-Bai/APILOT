import tornado.ioloop
import tornado.web
import tornado.websocket

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    clients = set()

    def open(self):
        self.clients.add(self)
        print("WebSocket opened.")

    def on_message(self, message):
        print(f"Message received: {message}")
        for client in self.clients:
            if client != self:
                client.write_message(message)

    def on_close(self):
        self.clients.remove(self)
        print("WebSocket closed.")

def make_app():
    return tornado.web.Application([
        (r'/websocket', WebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("WebSocket server started on ws://localhost:8888/websocket")
    tornado.ioloop.IOLoop.current().start()
