import tornado

def clear_ioloop(loop):
    loop.clear()

# Usage
loop = tornado.ioloop.IOLoop.current()
clear_ioloop(loop)
