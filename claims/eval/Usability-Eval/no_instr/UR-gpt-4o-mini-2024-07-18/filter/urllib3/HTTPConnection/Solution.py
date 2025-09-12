import urllib3

class HTTPConnection:
    def __init__(self, host, port=None, timeout=None, source_address=None, blocksize=8192):
        # Parse the host to extract port if necessary
        if ':' in host:
            host, port = host.split(':', 1)
            port = int(port)

        if port is None:
            port = 80  # Default HTTP port

        self.host = host
        self.port = port
        self.timeout = timeout
        self.source_address = source_address
        self.blocksize = blocksize
        self.connection = None

    def connect(self):
        self.connection = urllib3.HTTPConnectionPool(
            host=self.host,
            port=self.port,
            timeout=self.timeout,
            source_address=self.source_address,
            blocksize=self.blocksize
        )

    def close(self):
        if self.connection:
            self.connection.close()

# Example usage
if __name__ == "__main__":
    conn = HTTPConnection('example.com')
    conn.connect()
    print("Connected to", conn.host, "on port", conn.port)
    conn.close()
