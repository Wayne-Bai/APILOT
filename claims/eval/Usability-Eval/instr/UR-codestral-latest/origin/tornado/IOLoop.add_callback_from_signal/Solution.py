import tornado.ioloop

def callback():
    # Your custom logic here
    print("Callback function executed")

def schedule_callback():
    io_loop = tornado.ioloop.IOLoop.current()
    io_loop.add_callback(callback)

# Start the I/O loop
tornado.ioloop.IOLoop.current().start()
