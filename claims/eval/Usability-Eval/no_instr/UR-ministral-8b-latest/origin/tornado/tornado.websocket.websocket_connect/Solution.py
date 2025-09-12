import tornado.websocket
import tornado.ioloop
import tornado.web

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print('A new WebSocket connection is created')
        self.write_message({"event": "connection"})

    def on_message(self, message):
        print(f'Received message: {message}')
        # Echo the message back to the client
        self.write_message("属性反转，但我需要实时做@endsectionend")

    def on_close(self):
        print('WebSocket connection is closed')

def make_app():
    return tornado.web.Application([
        (r'/ws', WebSocketHandler),
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(8888)  # You can change the port number as needed
    tornado.ioloop.IOLoop.current().start()
