import tornado.web
import datetime

class MyHandler(tornado.web.RequestHandler):
    def get(self):
        cookie_name = "session"
        cookie_value = "user_id_123"
        self.set_secure_cookie(cookie_name, cookie_value, expires_days=1)  # Expiry is set to one day
        self.write("Cookie has been set securely.")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", MyHandler),
    ], cookie_secret="YOUR_SECRET_KEY_HERE")

    app.listen(8888)
    print("Server running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
