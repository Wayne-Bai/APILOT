import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # URL to redirect the user for OAuth authorization
        oauth_url = "https://example.com/oauth/authorize"
        
        # Redirecting user to the OAuth authorization URL
        self.redirect(oauth_url)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server is running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
