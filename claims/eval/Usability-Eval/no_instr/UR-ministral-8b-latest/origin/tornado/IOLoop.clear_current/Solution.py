import tornado.ioloop
import threading

def clear_ioloop():
    tornado.ioloop.IOLoop.current().clear()  # Clear the current IOLoop for the current thread
    print("IOLoop cleared for the current thread.")

# Ensure ioloop is being controlled by a specific thread
def run_in_thread():
    thread = threading.Thread(target=clear_ioloop)
    thread.start()
    thread.join()

if __name__ == "__main__":
    run_in_thread()
    tornado.ioloop.IOLoop.current().start()
