import tornado.ioloop
import tornado.web
import tornado.websocket
import json

# Define a WebSocket handler
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    # Handle new WebSocket connection
    def open(self):
        print("New connection established")

    # Handle incoming messages
    def on_message(self, message):
        # Handle the incoming message
        print("Received message from client: " + message)

        # Send a response back to the client
        response = "Server response: " + message
        self.write_message(response)

    # Handle WebSocket connection close
    def on_close(self):
        print("Connection closed")

    # Handle any errors
    def on_error(self, error):
        print("Error occurred: " + str(error))

# Define main application
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/websocket", WebSocketHandler)
        ]

        # Set up the Tornado application settings
        settings = {
            "template_path": ".",
            "static_path": ".",
            "debug": True
        }

        super(Application, self).__init__(handlers, **settings)

# Main function to start the server
if __name__ == "__main__":
    app = Application()
    app.listen(8888)
    print("Server is running at http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
