import tornado.web
from tornado import escape

class CookieHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        # Get the user from the session
        self.get_session()
        return self._current_user

    @tornado.web.authenticated
    def get(self):
        # Check if the cookie is valid and belongs to the current user
        cookie = self.get_signed_cookie('my-auth-token')
        if not cookie:
            return None

        user = self.get_current_user()
        if user and user.id == escape.xhtml_escape(cookie['id']):
            # The cookie is valid, so return it
            return cookie
        else:
            # The cookie is not valid or does not belong to the current user
            return None
