import tornado.ioloop
import tornado.websocket

class SimpleWebSocketClient(tornado.websocket.WebSocketClientConnection):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        print("Received message: {}".format(message))
        # Example of sending a message after receiving one
        self.write_message("Hello from client!")

    def on_close(self):
        print("WebSocket closed")

    def on_error(self, error):
        print("Error: {}".format(error))

def main():
    # Substitute 'ws://example.com/websocket' with the actual server's WebSocket URL
    websocket_url = 'ws://example.com/websocket'
    
    client = SimpleWebSocketClient(websocket_url)
    client.connect()

    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
