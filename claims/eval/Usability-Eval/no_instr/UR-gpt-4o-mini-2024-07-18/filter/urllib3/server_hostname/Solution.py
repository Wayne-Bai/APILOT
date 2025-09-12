import urllib3

class Server:
    def __init__(self, hostname=None):
        self.hostname = hostname

    def get_hostname(self):
        return self.hostname

# Example usage
server = Server("example.com")
print(server.get_hostname())  # Output: example.com

server_none = Server()
print(server_none.get_hostname())  # Output: None
