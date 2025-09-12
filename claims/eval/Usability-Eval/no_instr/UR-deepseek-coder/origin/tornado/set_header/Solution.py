import tornado.web

class SetHeaderHandler(tornado.web.RequestHandler):
    def get(self):
        header_name = "X-Custom-Header"
        header_value = "Custom Value"
        
        # Set the response header
        self.set_header(header_name, header_value)
        
        # Optionally, you can set more headers
        self.set_header("Content-Type", "text/plain")
        
        # Write the response body
        self.write("Header set successfully!")

# Define the application
application = tornado.web.Application([
    (r"/set_header", SetHeaderHandler),
])

# Start the server
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
