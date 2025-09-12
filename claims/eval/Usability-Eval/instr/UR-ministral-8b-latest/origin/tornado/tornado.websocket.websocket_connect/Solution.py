import tornado.ioloop
import tornado.web
import tornado.websocket
import json

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("New websocket connection")
        self.x = 0

    def on_message(self, message):
        print("Received message: {message}")
        self.x += int(message)  # Parse the message as an integer
        self.write_message({"result": self.x})

    def on_close(self):
        print("Connection closed")

def make_app():
    return tornado.web.Application([
        (r'/ws', WebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
