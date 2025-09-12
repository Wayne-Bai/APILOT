import tornado.ioloop

def clear_ioloop():
    loop = tornado.ioloop.IOLoop.current()
    loop.clear_current()

# Example usage:
clear_ioloop()
