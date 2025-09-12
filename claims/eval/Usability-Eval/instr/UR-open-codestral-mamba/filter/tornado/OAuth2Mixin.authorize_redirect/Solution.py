import tornado.ioloop
import tornado.web
import tornado.auth
import tornado.httpserver
import tornado.httpclient

class MainHandler(tornado.web.RequestHandler, tornado.auth.OAuth2Mixin):
    def get(self):
        if self.get_argument('code', False):
            self.get_token(self.async_callback(self.on_token))
            return
        else:
            self.authorize_redirect(
                self.settings['oauth_settings']['redirect_uri'],
                self.settings['oauth_settings']['scope'],
                client_id=self.settings['oauth_settings']['client_id'])

    def on_token(self, access):
        # Here you can save the obtained access tokens, then redirect or finish the request as needed.
        print('Access token received:', access)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler, {
            'oauth_settings': {
                'client_id': 'your_client_id',
                'client_secret': 'your_client_secret',
                'redirect_uri': 'https://your_redirect_uri',
                'scope': ['Scope1', 'Scope2'],     # replace with requested scope(s)
            },
            'headers': {
                'Accept-Encoding': 'gzip',
            }
        })
    ],compress=True)

def main():
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
