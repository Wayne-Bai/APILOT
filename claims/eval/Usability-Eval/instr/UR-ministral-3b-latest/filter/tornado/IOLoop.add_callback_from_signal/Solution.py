import tornado.ioloop
import tornado.web

def test_callback():
    print("Callback called")

class MainHandler(tornado.ioloop.PeriodicCallback):
    def __init__(self, loop, schedule_frequency):
        super(MainHandler, self).__init__(loop, schedule_frequency)
        self.add_callback(test_callback)

class MyApplication(tornado.web.Application):
    def __init__(self):
        handlers = [("/callback", PeriodicCallback)]
        super(MyApplication, self).__init__(handlers)
        self.loop = tornado.ioloop.IOLoop.current()
        self.add_callback(test_callback)
        self.callback = tornado.ioloop.PeriodicCallback(
            self.loop, callback=test_callback, first_run=False, repeat=True, limit=None, replace=True, id=None)

if __name__ == "__main__":
    app = MyApplication()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
