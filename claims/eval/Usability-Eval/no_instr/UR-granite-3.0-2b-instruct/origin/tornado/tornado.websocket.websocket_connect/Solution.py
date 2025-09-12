import tornado.ioloop
import tornado.web
import websockets

class WebSocketHandler(tornado.web.RequestHandler):
    async def open(self):
        self.write_message("Client connected")

    async def on_message(self, message):
        print(f"Received message: {message}")

    async def close(self):
        self.write_message("Client disconnected")

async def create_websocket_server():
    uri = "ws://127.0.0.1:8888"
    await websockets.serve(WebSocketHandler.on_message, uri)

if __name__ == '__main__':
    tornado.ioloop.run_until_complete(create_websocket_server())
