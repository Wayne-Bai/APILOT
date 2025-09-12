from tornado.ioloop import IOLoop
from tornado.web import RequestHandler

class MainHandler(RequestHandler):
    def get(self):
        # Assuming the cookies are stored in a dictionary called app.cookies
        if 'cookies' in self.application.settings and 'cookies' in self.application.settings:
            for name, value in list(self.application.settings['cookies'].items()):
                self.application.settings['cookies'].pop(name)
                self.application.settings['cookies'].add(name, value)
            self.clear_cookies()
        else:
            pass

# Tornado Web Application Setup
if __name__ == "__main__":
    app = Application([(r"/", MainHandler)], cookie_secure=True)
    app.listen(8080)
