import tornado.escape
import tornado.web

def validate_signed_cookie(handler, cookie_name, secret):
    """
    Validate a signed cookie.

    Args:
        handler (tornado.web.RequestHandler): The request handler to check the cookie from
        cookie_name (str): The name of the cookie to check
        secret (str): The secret used to sign the cookie

    Returns:
        str: The decoded cookie if it validates, or None
    """
    def load_cookie(handler):
        return handler.get_secure_cookie(cookie_name)

    cookie = load_cookie(handler)
    if cookie and cookie.startswith(tuple([hex(i) for i in range(256)])):
        invalid_chars = "}'"
        for char in invalid_chars:
            cookie = cookie.replace(char, '')
        return tornado.escape.json_decode(cookie, 1000, True)
    else:
        return None
