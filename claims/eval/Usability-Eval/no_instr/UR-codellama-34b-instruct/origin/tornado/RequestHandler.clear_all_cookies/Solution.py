
import tornado.web

class CookieDeletionHandler(tornado.web.RequestHandler):
    def get(self):
        # Get the list of cookies from the request
        cookies = self.request.cookies
        
        # Delete each cookie in the list
        for cookie in cookies:
            self.delete_cookie(cookie)
            
        # Return a success response to the user
        self.write("All cookies deleted!")
