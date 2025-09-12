import tornado.ioloop
import tornado.web
import tornado.websocket

class MyHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        # This handler class method is called when a new websocket connection is
        # established
        print("New websocket connection")
        self.global_messages = ["Welcome"]
        self.global_app = False

    def on_message(self, message):
        if message == 'hello':
            return
        elif message == 'fetch':
            if self.global_messages:
                self.write_messages(self.global_messages)
                self.write_message('Finished fetching')

    def on_close(self):
        # This handler class method is called when a websocket connection is
        # closed
        self.global_app = True
        print("Closed websocket connection")

    def on_error(self, error):
        self.on_close()
        print("Occurred error, am closing now")

class TornadoApp(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/mywebsocket', MyHandler)
        ]
        setting = None
        super(TornadoApp, self).__init__(handlers, setting)

if __name__ == "__main__":
    app = TornadoApp()
    app.listen(8888)
    print("Server started")
    tornado.ioloop.IOLoop.current().start()
