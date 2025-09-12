import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # Set a message to show that we are here
        self.write("Welcome! Let's delete your cookies.")

    def post(self):
        # Get all cookies sent with the request
        cookies = self.request.cookies
        
        # Iterate through all cookies and delete them
        for cookie_name in cookies:
            self.clear_cookie(cookie_name)

        # Send a response indicating cookies have been cleared
        self.write("All cookies have been deleted.")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
