import tornado.httpserver
import tornado.websocket
import tornado.ioloop

# Define a client websocket handler
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        # Reverse the received message and send it back
        reversed_message = message[::-1]
        self.write_message(reversed_message)

    def on_close(self):
        print("WebSocket closed")

# Application entry point
application = tornado.web.Application([
    (r'/ws', WSHandler),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
