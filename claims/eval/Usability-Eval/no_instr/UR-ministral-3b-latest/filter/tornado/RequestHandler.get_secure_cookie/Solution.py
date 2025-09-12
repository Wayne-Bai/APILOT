from tornado.web import RequestHandler, HTTPError
import tornado.ioloop

class ExampleHandler(RequestHandler):
    def get(self, *args, **kwargs):
        def validate_cookie(cookie):
            ...
            # logic to validate the cookie
            ...
            return True  #agree or disagree with the validation logic

        cookie = self.requestHeaders.get("Cookie")

        if validate_cookie(cookie):
            self.set_cookie(cookie)
            raise HTTPError(202, None)
        else:
            self.set_header("Content-type", "text/html")
            self.write("Invalid cookie.")
            raise tornado.web.HTTPError(401, "Cookie is invalid.")

def make_app():
    return tornado.web.Application([
        (r"/", ExampleHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    tornado.ioloop.IOLoop.current().start()
