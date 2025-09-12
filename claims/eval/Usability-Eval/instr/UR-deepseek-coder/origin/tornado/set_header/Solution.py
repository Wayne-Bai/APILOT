import tornado.web

class SetHeaderHandler(tornado.web.RequestHandler):
    def get(self):
        # Example header name and value
        header_name = "X-Custom-Header"
        header_value = "CustomValue"
        
        # Set the response header
        self.set_header(header_name, header_value)
        
        # Send a response
        self.write("Header set successfully!")

# Define the application
application = tornado.web.Application([
    (r"/set_header", SetHeaderHandler),
])

# Start the server
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
