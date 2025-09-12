import tornado
from tornado.websocket import WebSocketHandler
class MainHandler(WebSocketHandler):
    async def open(self):
        # Websocket connection has been established
        pass
    
    async def on_message(self, message):
        # New message has been received from the client
        pass
    
    async def on_close(self):
        # Websocket connection has been closed
        pass

# Set up the application
application = tornado.web.Application([
    (r'/', MainHandler),
])

# Start the server
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
