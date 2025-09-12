
import tornado.wsgi

# Create a WSGI application
app = tornado.wsgi.WSGIApplication(my_app)

# Run the application on Tornado's HTTP server
http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(8000)
tornado.ioloop.IOLoop.current().start()
