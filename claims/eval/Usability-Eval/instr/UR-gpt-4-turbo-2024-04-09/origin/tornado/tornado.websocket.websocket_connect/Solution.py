import tornado.ioloop
import tornado.websocket

class SimpleWebSocketClient(tornado.websocket.WebSocketClientConnection):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        print("Received message: {}".format(message))

    def on_close(self):
        print("WebSocket closed")

    def write_message(self, message):
        super(SimpleWebSocketClient, self).write_message(message)

def connect_to_websocket(url):
    ws_app = tornado.websocket.websocket_connect(url)
    return ws_app

if __name__ == "__main__":
    server_url = "ws://example.com/websocket"
    app = connect_to_websocket(server_url)

    ioloop = tornado.ioloop.IOLoop.instance()
    
    # Keeping the WebSocket connection open until manually stopped or an exception occurs
    try:
        ioloop.start()
    except KeyboardInterrupt:
        ioloop.stop()
        print("Connection closed by user.")
