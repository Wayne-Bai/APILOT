
import tornado.httputil

def sign_cookie(cookie):
    # Generate a signature using the secret key
    signature = hmac.new(secret_key, msg=cookie, digestmod=hashlib.sha256).hexdigest()

    # Add the signature to the cookie as a new attribute
    cookie['signature'] = signature

    return cookie
