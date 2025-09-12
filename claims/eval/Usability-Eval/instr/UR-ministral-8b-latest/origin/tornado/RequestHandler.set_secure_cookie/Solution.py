import tornado.ioloop
import tornado.web
import time
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

class SecureHandler(tornado.web.RequestHandler):
    secret_key = "your-secret-key"

    def get(self):
        s = Serializer(self.secret_key, expires_in=3600)
        data = {"user_id": "example_user_id"}

        token = s.dumps(data).decode('utf-8')

        self.set_secure_cookie("auth_token", token)
        self.write({"message": "Secure cookie set"})

    def post(self):
        token = self.get_secure_cookie("auth_token")

        if token is not None:
            s = Serializer(self.secret_key, expires_in=3600)
            try:
                data = s.loads(token)
                self.write({"message": "Valid token", "user_id": data["user_id"]})
            except:
                self.write({"message": "Invalid token"})
        else:
            self.write({"message": "No token"})

def make_app():
    return tornado.web.Application([
        (r"/", SecureHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
