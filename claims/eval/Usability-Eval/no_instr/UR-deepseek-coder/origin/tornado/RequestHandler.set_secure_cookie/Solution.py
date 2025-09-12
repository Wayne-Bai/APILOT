import tornado.web
import hashlib
import hmac
import time

class CookieSignerHandler(tornado.web.RequestHandler):
    def get(self):
        # Example cookie value
        cookie_value = "user_session_12345"
        
        # Sign the cookie with a secret key
        secret_key = "your_secret_key"
        timestamp = str(int(time.time()))
        signature = hmac.new(secret_key.encode(), (cookie_value + timestamp).encode(), hashlib.sha256).hexdigest()
        
        # Combine the cookie value, timestamp, and signature
        signed_cookie = f"{cookie_value}|{timestamp}|{signature}"
        
        # Set the signed cookie
        self.set_cookie("signed_cookie", signed_cookie)
        
        self.write("Cookie signed and set!")

    def post(self):
        # Retrieve the signed cookie
        signed_cookie = self.get_cookie("signed_cookie")
        
        if signed_cookie:
            cookie_value, timestamp, signature = signed_cookie.split("|")
            
            # Verify the signature
            secret_key = "your_secret_key"
            expected_signature = hmac.new(secret_key.encode(), (cookie_value + timestamp).encode(), hashlib.sha256).hexdigest()
            
            if hmac.compare_digest(signature, expected_signature):
                self.write(f"Cookie verified: {cookie_value}")
            else:
                self.write("Cookie signature verification failed!")
        else:
            self.write("No signed cookie found!")

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/sign_cookie", CookieSignerHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
