import tornado.ioloop

def clear_ioloop():
    ioloop = tornado.ioloop.IOLoop.current()
    ioloop.clear()

if __name__ == "__main__":
    clear_ioloop()
