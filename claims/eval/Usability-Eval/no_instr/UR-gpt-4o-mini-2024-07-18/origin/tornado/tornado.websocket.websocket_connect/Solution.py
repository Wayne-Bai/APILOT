import tornado.ioloop
import tornado.web
import tornado.websocket

class WSHandler(tornado.websocket.WebSocketHandler):
    clients = set()

    def open(self):
        self.clients.add(self)
        print("WebSocket opened")

    def on_message(self, message):
        print(f"Message received: {message}")
        for client in self.clients:
            if client != self:
                client.write_message(message)

    def on_close(self):
        self.clients.remove(self)
        print("WebSocket closed")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<html><body><h1>WebSocket Example</h1><script>"
                   "var ws = new WebSocket('ws://localhost:8888/ws');"
                   "ws.onmessage = function(event) { console.log(event.data); };"
                   "ws.onopen = function() { ws.send('Hello, Server!'); };"
                   "</script></body></html>")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/ws", WSHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
