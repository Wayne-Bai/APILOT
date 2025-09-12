import tornado.ioloop
import tornado.web
from tornado.options import define, options

# Define a port number for the server to run on
define("port", default=8000, help="Port to run the server on")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # Get all the cookies from the request
        cookies = self.request.cookies
        
        # Delete each cookie by setting its expiration date to 0
        for cookie in cookies:
            self.set_secure_cookie(cookie, '')
            self.clear_cookie(cookie)
        
        # Send a response back to the client
        self.write("Cookies deleted: " + str(cookies.keys()))

def main():
    options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
    ], cookie_secret="your-secret-key")
    application.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
