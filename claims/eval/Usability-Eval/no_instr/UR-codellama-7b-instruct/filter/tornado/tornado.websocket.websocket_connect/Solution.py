
import tornado.websocket

class MyWebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        # handle incoming messages
        pass

    def on_close(self):
        print("WebSocket closed")
