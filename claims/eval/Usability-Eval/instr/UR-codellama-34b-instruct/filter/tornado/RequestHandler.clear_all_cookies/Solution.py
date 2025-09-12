
import tornado.web

class DeleteCookiesHandler(tornado.web.RequestHandler):
    def get(self):
        # Get a list of all cookies from the request
        cookies = self.request.cookies.keys()

        # Iterate over the list and delete each cookie
        for cookie in cookies:
            self.clear_cookie(cookie)

        # Return a success response
        return self.write("All cookies deleted")
