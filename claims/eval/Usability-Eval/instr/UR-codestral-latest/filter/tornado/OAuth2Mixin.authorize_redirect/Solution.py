import tornado.ioloop
import tornado.web

class OAuthHandler(tornado.web.RequestHandler):
    async def get(self):
        # Request for OAuth authorization
        self.redirect(f'https://service_provider.com/oauth/authorize?client_id={client_id}&scope={scope}&redirect_uri={redirect_uri}')

def make_app():
    return tornado.web.Application([
        (r"/oauth/authorize", OAuthHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
