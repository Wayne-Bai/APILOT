
import tornado.web

class AuthenticateHandler(tornado.web.RequestHandler):
    def get_cookie(self, name: str) -> bytes:
        """
        Returns the value of a signed cookie if it validates, or None.
        :param name: The name of the cookie to retrieve
        :return: The signed cookie value, or None if the cookie is invalid
        """
        cookie_value = self.get_secure_cookie(name)
        try:
            cookie_signature = tornado.escape.url_unescape(self.request.headers["Cookie"].split(";")[0])
            return tornado.escape.url_unescape(cookie_value) + b":" + cookie_signature
        except (IndexError, KeyError):
            return None
