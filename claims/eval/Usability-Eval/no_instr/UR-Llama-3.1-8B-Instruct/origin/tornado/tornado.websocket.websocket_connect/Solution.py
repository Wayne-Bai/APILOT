
import tornado.ioloop
import tornado.web
import tornado.websocket

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("Client connected")
        self.clients = set()

    def on_connect(self):
        self.clients.add(self)

    def on_close(self):
        self.clients.remove(self)
        print("Client disconnected")

    def on_message(self, message):
        # Broadcast the message to all connected clients
        for client in self.clients:
            if client!= self:
                client.write_message(message)

def make_app():
    return tornado.web.Application([
        (r"/websocket", WebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
