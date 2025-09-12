import tornado.ioloop

def clear_ioloop():
    tornado.ioloop.IOLoop.current().clear_current()