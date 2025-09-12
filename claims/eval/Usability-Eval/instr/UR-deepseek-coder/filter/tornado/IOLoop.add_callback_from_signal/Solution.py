import tornado.ioloop

def callback():
    print("Callback executed on the next I/O loop iteration.")

def main():
    # Schedule the callback to be called on the next I/O loop iteration
    tornado.ioloop.IOLoop.current().add_callback(callback)
    
    # Start the I/O loop
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
