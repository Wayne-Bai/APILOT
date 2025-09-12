import tornado.ioloop

def clear_ioloop_current_thread():
    current_ioloop = tornado.ioloop.IOLoop.current()
    current_ioloop.clear_current()

if __name__ == "__main__":
    clear_ioloop_current_thread()
