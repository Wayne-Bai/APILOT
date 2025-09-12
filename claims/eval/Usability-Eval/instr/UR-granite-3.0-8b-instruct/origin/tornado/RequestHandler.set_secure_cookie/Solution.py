import tornado.escape
import tornado.web
import time

# Secret key for signing the cookie
SECRET_KEY = "your_secret_key_here"

# Expiration time for the cookie in seconds
EXPIRATION_TIME = 3600  # 1 hour

# Generate a timestamp for the cookie
timestamp = int(time.time())

# Create a signed and timestamped dictionary
signed_dict = tornado.escape.signed_dict({"timestamp": timestamp}, key=SECRET_KEY)

# Convert the timestamp to an expiration time
expiry = tornado.escape.timestamp_to_expiry(signed_dict["timestamp"])

# Now you can set the signed and timestamped cookie
# For example, in a Tornado Handler:
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_secure_cookie("cookie_name", signed_dict, expires_in=EXPIRATION_TIME, http_only=True)
