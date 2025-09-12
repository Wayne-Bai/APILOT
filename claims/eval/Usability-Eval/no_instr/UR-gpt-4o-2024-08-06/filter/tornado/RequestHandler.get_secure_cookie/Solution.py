import tornado.web
import tornado.ioloop

class MainHandler(tornado.web.RequestHandler):
    # Define a cookie secret for signing cookies
    COOKIE_SECRET = "your_secure_secret_key_here"
    
    def get(self):
        # Try to retrieve the signed cookie
        cookie_value = self.get_secure_cookie("user_cookie")
        
        # Check if the cookie was successfully retrieved and validated
        if cookie_value is not None:
            self.write(f"Cookie is valid: {cookie_value.decode('utf-8')}")
        else:
            self.write("No valid cookie found.")
    
    def set_signed_cookie(self, name, value):
        # Set a signed cookie using self.write_secure_cookie method
        self.set_secure_cookie(name, value)
        
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], cookie_secret=MainHandler.COOKIE_SECRET)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server started at http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
