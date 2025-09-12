import tornado.web
import time

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # Create a new cookie to store the user's ID
        user_id_cookie = tornado.web.CookieSigned(
            "user_id",
            "my_cookie_secret",
            expires_days=30,
        )

        # Set the user's ID in the cookie
        user_id_cookie.set_cookie(self)

        # Generate a timestamp for the cookie
        timestamp = str(int(time.time()))

        # Sign the cookie with a timestamp
        signed_cookie = user_id_cookie.sign(timestamp)

        # Set the signed cookie
        self.set_cookie("signed_cookie", signed_cookie)

        # Display the user's ID and the signed cookie
        self.write("User ID: {}".format(self.get_cookie("user_id")))
        self.write("Signed Cookie: {}".format(self.get_cookie("signed_cookie")))
