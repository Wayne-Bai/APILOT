
import tornado.ioloop

def clear_io_loop():
    tornado.ioloop.IOLoop.clear(tornado.platform.asyncio.AsyncOloop)
