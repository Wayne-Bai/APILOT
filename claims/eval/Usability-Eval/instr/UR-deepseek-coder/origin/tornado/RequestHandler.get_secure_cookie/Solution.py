import tornado.web
import tornado.escape

class SecureCookieHandler(tornado.web.RequestHandler):
    def get_secure_cookie(self, name):
        cookie = self.get_cookie(name)
        if cookie is None:
            return None
        
        # Assuming the cookie is signed with a secret key
        secret_key = "your_secret_key"
        try:
            decoded_cookie = tornado.escape.url_unescape(cookie)
            # Verify the signature
            if tornado.escape.utf8(decoded_cookie) == tornado.escape.utf8(cookie):
                return decoded_cookie
        except Exception as e:
            print(f"Error decoding cookie: {e}")
        
        return None

    def get(self):
        cookie_name = "your_cookie_name"
        cookie_value = self.get_secure_cookie(cookie_name)
        if cookie_value:
            self.write(f"Valid cookie: {cookie_value}")
        else:
            self.write("No valid cookie found.")

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", SecureCookieHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
