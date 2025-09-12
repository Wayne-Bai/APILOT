import tornado.web
import tornado.ioloop
import tornado.httpclient

class OAuthHandler(tornado.web.RequestHandler):
    def get(self):
        # Replace 'YOUR_CLIENT_ID' and 'YOUR_REDIRECT_URI' with your actual values
        client_id = 'YOUR_CLIENT_ID'
        redirect_uri = 'YOUR_REDIRECT_URI'

        # Generate the authorization URL
        authorization_url = f'https://api.example.com/oauth/authorize?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}'

        # Redirect the user to the authorization URL
        self.redirect(authorization_url)

def make_app():
    return tornado.web.Application([
        (r'/', OAuthHandler),
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
