import tornado.ioloop
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        callback = self.request.callback
        if callback:
            callback()
        else:
            self.write("No callback provided")

class MainHandler(BaseHandler):
    def get(self):
        callback = self.get_callback()
        self.callback(callback)
        super(MainHandler, self).get()
        # This will proceed as normal and call get() which triggers callback

    def get_callback(self):
        # Dummy callback function for demonstration
        def callback():
            self.write("Callback is called!")
        return callback

def main():
    app = tornado.web.Application([
        (r"/", MainHandler),
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
