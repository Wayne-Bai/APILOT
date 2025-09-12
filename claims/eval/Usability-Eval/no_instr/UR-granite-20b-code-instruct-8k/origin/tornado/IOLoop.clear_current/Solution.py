
import tornado.ioloop
# Get the current IOLoop
io_loop = tornado.ioloop.IOLoop.current()
# Clear the IOLoop
io_loop.clear_current()
