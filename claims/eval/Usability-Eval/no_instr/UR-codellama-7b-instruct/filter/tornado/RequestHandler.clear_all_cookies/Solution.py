
import http.client
from tornado.httpclient import HTTPCookie

# Set up the client
client = http.client.HTTPConnection("www.example.com")

# Set up the cookie headers
cookie_headers = []
for name, value in request.cookies:
    cookie_headers.append(f"{name}={value}")

# Make a GET request and delete all cookies
response = client.get("/", headers=cookie_headers)
