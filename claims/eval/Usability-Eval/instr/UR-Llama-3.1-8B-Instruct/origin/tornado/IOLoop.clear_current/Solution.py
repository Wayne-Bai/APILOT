import tornado.ioloop

def clear_ioloop():
    """
    Clears the IOLoop for the current thread.
    """
    ioloop = tornado.ioloop.IOLoop.current()
    ioloop.clear()

if __name__ == "__main__":
    clear_ioloop()
