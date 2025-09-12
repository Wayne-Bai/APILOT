import tornado.ioloop
import tornado.web
import tornado.auth
import tornado.httpclient

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect(self.reverse_url('oauth'))

class OAuthHandler(tornado.web.RequestHandler, tornado.auth.OAuth2Mixin):
    async def get(self):
        if self.get_argument('code', False):
            user = await self.get_authenticated_user(
                redirect_uri='http://your-callback-url',
                client_id='your-client-id',
                client_secret='your-client-secret',
                code=self.get_argument('code'))
            # Use the user object to create a session
            self.set_current_user(user)
            self.redirect('/')
        else:
            self.authorize_redirect(
                redirect_uri='http://your-callback-url',
                client_id='your-client-id',
                scope=['scope1', 'scope2'],
                response_type='code',
                extra_params={'approval_prompt': 'auto'})

    def set_current_user(self, user):
        self.set_secure_cookie('user', tornado.escape.json_encode(user))

settings = {
    'debug': True,
    'login_url': '/login'
}

application = tornado.web.Application([
    (r'/', MainHandler),
    (r'/oauth', OAuthHandler, {'prefix': '/oauth2'}),
], **settings)

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
