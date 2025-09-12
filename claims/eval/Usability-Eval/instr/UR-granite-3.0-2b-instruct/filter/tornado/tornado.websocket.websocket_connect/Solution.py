import tornado.ioloop
import tornado.web

class WebSocketHandler(tornado.web.WebSocketHandler):
    def on_connect(self):
        print("Client connected")

    def on_message(self, message):
        print("Received message:", message)

    def on_close(self):
        print("Client disconnected")

def make_app():
    return tornado.web.Application([
        (r"/ws", WebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().run_until_complete(app)
