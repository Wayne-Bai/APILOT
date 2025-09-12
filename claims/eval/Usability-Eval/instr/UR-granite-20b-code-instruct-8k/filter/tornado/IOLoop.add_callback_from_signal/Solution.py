import tornado.ioloop

def my_callback():
    print("This is called on the next I/O loop iteration.")

tornado.ioloop.IOLoop.current().add_callback(my_callback)
tornado.ioloop.IOLoop.current().start()
