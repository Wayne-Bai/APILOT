import tornado.ioloop
import tornado.futures

def callback():
    print("This will be printed on the next I/O loop iteration.")

def main():
    with tornado.ioloop.Future() as fut:
        fut.add_done_callback(callback)
        tornado.ioloop.IOLoop.current().run_until_complete(fut)

if __name__ == '__main__':
    main()
