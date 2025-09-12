import tornado.ioloop
import tornado.web
from tornado_oauth import OAuth2

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        oauth = OAuth2(
            consumer_key='your_consumer_key',
            consumer_secret='your_consumer_secret',
            request_token_params={
                'oauth_callback': 'http://localhost:8888/result'
            },
            access_token_params={
                'oauth_token': 'your_access_token'
            }
        )

        self.set_header('Location', oauth.authorization_url)

def run():
    app = tornado.web.Application([
        (r'/', MainHandler),
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().run_until_complete(app)

if __name__ == '__main__':
    run()
