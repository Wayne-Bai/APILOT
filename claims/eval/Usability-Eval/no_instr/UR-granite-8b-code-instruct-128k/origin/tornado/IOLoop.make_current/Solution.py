
import tornado

class MyIOLoop(tornado.ioloop.IOLoop):
    pass

my_ioloop = MyIOLoop.instance()
