import urllib3
import ssl

class HTTPSConnection(urllib3.connection.HTTPConnection):
    default_port = 443

    def __init__(self, host, port=None, context=None, **kwargs):
        super().__init__(host, port or self.default_port, **kwargs)
        self.context = context or ssl.create_default_context()

        # wrap the socket using SSL
        self.sock = self.context.wrap_socket(self.sock, server_hostname=host)

# Example usage
if __name__ == "__main__":
    context = ssl.create_default_context()  # Custom SSL context can be configured here
    conn = HTTPSConnection("example.com", context=context)
    conn.request("GET", "/")
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()
    print(data)
