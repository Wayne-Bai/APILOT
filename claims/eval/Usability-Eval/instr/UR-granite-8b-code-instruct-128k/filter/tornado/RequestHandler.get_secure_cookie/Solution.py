import tornado

def get_signed_cookie(cookie, key, max_age=None):
    """Returns the given signed cookie if it validates, or None."""
    # Use the tornado.web.get_cookie function to validate the cookie
    # and return the corresponding value. If the cookie is not valid,
    # return None.
    return tornado.web.get_cookie(cookie, key, max_age)
