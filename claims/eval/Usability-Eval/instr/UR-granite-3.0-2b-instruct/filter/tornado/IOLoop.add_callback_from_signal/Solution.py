import tornado.ioloop
import tornado.callback

def callback_function():
    print("Callback function called!")

def main():
    tornado.ioloop.IOLoop.current().run_with_timeout(5.0, callback_function)

if __name__ == '__main__':
    main()
