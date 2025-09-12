import tornado.web
from tornado.options import options
from tornado.util import log
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.backoff import ExponentialBackOff

class TwitterAuthHandler(tornado.web.RequestHandler):
    def get(self):
        from tornado.oauth import TwitterOAuth
        OAuth = TwitterOAuth(
            consumer_key='your_consumer_key',
            consumer_secret='your_consumer_secret',
            access_token_key='your_access_token_key',
            access_token_secret='your_access_token_secret'
        )
        try:
            authorization_url, state = OAuth.request_token(
                'http://your_app_url/callback', state='state_value'
            )
            self.write({'url': authorization_url})
        except Exception as e:
            self.write({'error': str(e)})

    def post(self):
        from tornado.oauth import TwitterOAuth
        OAuth = TwitterOAuth(
            consumer_key='your_consumer_key',
            consumer_secret='your_consumer_secret',
            access_token_key='your_access_token_key',
            access_token_secret='your_access_token_secret'
        )
        authorization_url, state = self.request.args.get('authorization_url')
        code = self.request.args.get('code')
        try:
            token = OAuth.access_token(
                authorization_url, code, state='state_value'
            )
            self.write({'access_token': token.access_token})
        except Exception as e:
            self.write({'error': str(e)})

if __name__ == '__main__':
    options.parse_command_line()
    log.info('starting with port %s' % options.port)
    server = HTTPServer(TwitterAuthHandler)
    server.listen(options.port)
    IOLoop.current().run_until_complete(server)
    IOLoop.current().run_until_complete(server.close())
