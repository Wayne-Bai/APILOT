from tornado.web import RequestHandler, Application

# Subclass the tornado RequestHandler class
class CookieHandler(RequestHandler):
    def post(self):
        # Clear all cookies
        self.clear_all_cookies()
        self.write("All cookies deleted successfully!")

# Create an instance of the Tornado application
app = Application([
    (r"/clear_cookies", CookieHandler)
])

# Start the Tornado application
app.listen(8888)
