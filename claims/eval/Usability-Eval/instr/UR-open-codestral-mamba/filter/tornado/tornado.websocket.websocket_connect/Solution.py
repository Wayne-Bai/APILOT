import tornado.websocket
import tornado.httpserver
import tornado.ioloop

class MessageHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message("Message received: " + message)

    def on_close(self):
        print("WebSocket closed")

def make_app():
    return tornado.web.Application([
        (r"/websocket", MessageHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    print("Server started at http://localhost:8888/websocket")
    tornado.ioloop.IOLoop.current().start()
