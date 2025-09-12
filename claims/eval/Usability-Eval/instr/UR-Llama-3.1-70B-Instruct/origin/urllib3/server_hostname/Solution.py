import urllib3

class SocketInfo:
    def __init__(self, hostname=None, port=None):
        self.hostname = hostname
        self.port = port

    def __str__(self):
        return f"Hostname: {self.hostname}, Port: {self.port}"

def get_server_info():
    http = urllib3.PoolManager()
    try:
        r = http.request('GET', 'https://example.com')
        if r.status == 200:
            server_info = r.headers.get('Server')
            socket_info = SocketInfo()
            if 'localhost' in server_info or '127.0.0.1' in server_info:
                socket_info.hostname = None
            else:
                socket_info.hostname = server_info
            return socket_info
    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Example usage
server_info = get_server_info()
if server_info:
    print(server_info)
