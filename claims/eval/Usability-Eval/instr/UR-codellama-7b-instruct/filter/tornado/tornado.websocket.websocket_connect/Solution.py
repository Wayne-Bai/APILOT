
import tornado.websocket
from tornado import gen

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self, *args, **kwargs):
        self.ws = tornado.websocket.websocket(self)

    @gen.coroutine
    def on_message(self, message):
        if message == "Hello":
            self.write("Hi")

    @gen.coroutine
    def on_close(self, *args, **kwargs):
        print("Websocket connection closed")

    @gen.coroutine
    def check_origin(self, origin):
        return True
