import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options

from tornado.options import define, options
from tornado.web import RequestHandler
from twitterOAuth import TwitterOAuth

define("port", default=8888, help="run on the given port")

class LoginHandler(RequestHandler):
    def get(self):
        consumer_key = 'your_consumer_key'
        consumer_secret = 'your_consumer_secret'

        oauth = TwitterOAuth(consumer_key, consumer_secret)
        url = oauth.get_authorization_url()
        self.redirect(url)

class CallbackHandler(RequestHandler):
    def get(self, code):
        consumer_key = 'your_consumer_key'
        consumer_secret = 'your_consumer_secret'

        access_token, access_token_secret = None, None
        oauth = TwitterOAuth(consumer_key, consumer_secret)
        oauth.set_access_token(code, None)
        oauth.get_access_token_for_verb('get', 'user')
        access_token = oauth.access_token
        access_token_secret = oauth.access_token_secret

        user_data = oauth.get('user timeline')
        print(user_data)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/login", LoginHandler),
                                            (r'/callback', CallbackHandler)],
                                 debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
