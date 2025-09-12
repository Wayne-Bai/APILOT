
import urllib3

# Set up the URL for the proxied server
proxied_url = "http://example.com"

# Set up the port number for the proxied server
proxied_port = 8080

# Create a ProxyHandler and add it to a OpenerDirector
proxy_handler = urllib3.ProxyHandler({'http': 'http://localhost:{}'.format(proxied_port)})
opener = urllib3.OpenerDirector()
opener.add_handler(proxy_handler)

# Set up the proxy server
proxy_server = opener.open("http://localhost:{}/".format(8080), data=proxied_url)

# Start the proxy server
server = http.server.HTTPServer((proxied_ip, proxied_port), ProxyHandler)
server.serve_forever()
