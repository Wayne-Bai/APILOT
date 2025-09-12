import tornado.ioloop

def my_callback():
    print("Callback executed")

def schedule_callback():
    io_loop = tornado.ioloop.IOLoop.current()
    io_loop.add_callback(my_callback)

if __name__ == "__main__":
    schedule_callback()
    tornado.ioloop.IOLoop.current().start()
