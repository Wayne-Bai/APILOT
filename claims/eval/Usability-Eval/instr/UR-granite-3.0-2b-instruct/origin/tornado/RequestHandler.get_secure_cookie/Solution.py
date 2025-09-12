import tornado.web

class SignedCookieHandler(tornado.web.RequestHandler):
    def get(self):
        cookie_name = self.get_argument('cookie_name')
        cookie_value = self.get_argument('cookie_value')
        signature = self.get_argument('signature')

        # Assuming you have a function to validate the signature and cookie value
        is_valid = validate_signature_and_value(cookie_name, cookie_value, signature)

        if is_valid:
            self.set_header('Content-Type', 'application/octet-stream')
            self.set_body(cookie_value.encode('utf-8'))
        else:
            self.set_status(400)
            self.set_body('Invalid cookie')

def validate_signature_and_value(cookie_name, cookie_value, signature):
    # Implement your signature validation logic here
    # This is a placeholder function
    return True

app = tornado.web.Application([
    (r'/get_cookie', SignedCookieHandler),
])

if __name__ == '__main__':
    app.run()
