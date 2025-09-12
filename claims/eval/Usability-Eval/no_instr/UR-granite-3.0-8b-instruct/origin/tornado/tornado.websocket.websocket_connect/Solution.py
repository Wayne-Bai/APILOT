import tornado.ioloop
import tornado.websocket

class WebsocketClient(tornado.websocket.WebSocketClient):
    def on_message(self, message):
        print("Received message: ", message)

    def on_open(self):
        print("Websocket connected")

    def on_close(self):
        print("Websocket disconnected")

    def on_error(self, e):
        print("Websocket error: ", e)

def main():
    client = WebsocketClient("ws://example.com/websocket")
    client.connect()
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
