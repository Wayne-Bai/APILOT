import tornado.ioloop

def clear_current_ioloop():
    io_loop = tornado.ioloop.IOLoop.current()
    io_loop.clear_instance()

if __name__ == "__main__":
    clear_current_ioloop()
    print("IOLoop for the current thread cleared.")
