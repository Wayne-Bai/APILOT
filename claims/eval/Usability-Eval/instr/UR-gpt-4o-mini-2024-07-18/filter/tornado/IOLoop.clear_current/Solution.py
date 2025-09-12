import tornado.ioloop

def clear_ioloop():
    tornado.ioloop.IOLoop.current().stop()
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    clear_ioloop()
