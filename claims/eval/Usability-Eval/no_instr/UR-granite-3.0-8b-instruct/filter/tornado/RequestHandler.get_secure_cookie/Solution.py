import tornado.web
from tornado.cookie import SignedCookieJar

class MyHandler(tornado.web.RequestHandler):
    def get(self):
        jar = SignedCookieJar()
        signed_cookie = jar.get_signed_cookie(self.request, 'my_cookie')
        if signed_cookie:
            self.write(signed_cookie)
        else:
            self.write("No signed cookie found")
