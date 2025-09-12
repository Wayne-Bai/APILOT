import tornado.ioloop
import tornado.web
from tornado.options import define, options
import twitter

define("port", default=8080, help="Port number", type=int)

class TwitterHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "application/json")
        api = twitter.Api(consumer_key="your_consumer_key",
                          consumer_secret="your_consumer_secret",
                          access_token_key="your_access_token_key",
                          access_token_secret="your_access_token_secret")
        status = api.GetUser("your_screen_name")
        self.write(status.__dict__)

def make_app():
    return tornado.web.Application([
        (r"/twitter", TwitterHandler),
    ])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
