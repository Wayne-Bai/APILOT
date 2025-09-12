import tornado.ioloop
import tornado.web
import tornado.websocket

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    """Handles WebSocket connections"""
    
    clients = set()  # Store all connected clients
    
    def open(self):
        """Opens a new WebSocket connection"""
        self.clients.add(self)  # Add client to the set
        print(f"New connection: {self.request.remote_ip}")

    def on_message(self, message):
        """Handles incoming messages"""
        print(f"Received message: {message} from {self.request.remote_ip}")
        
        # Send the message to all connected clients (except the sender)
        for client in self.clients:
            if client!= self:
                client.write_message(message)

    def on_close(self):
        """Closes the WebSocket connection"""
        self.clients.remove(self)  # Remove client from the set
        print(f"Connection closed: {self.request.remote_ip}")

if __name__ == "__main__":
    application = tornado.web.Application([(r"/ws", WebSocketHandler)])
    application.listen(8765)  # Listen on port 8765
    tornado.ioloop.IOLoop.current().start()
