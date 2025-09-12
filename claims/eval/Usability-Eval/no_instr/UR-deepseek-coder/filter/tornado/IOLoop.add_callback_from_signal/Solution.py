import tornado.ioloop

def callback():
    print("Callback executed on the next I/O loop iteration.")

def main():
    io_loop = tornado.ioloop.IOLoop.current()
    io_loop.add_callback(callback)
    io_loop.start()

if __name__ == "__main__":
    main()
