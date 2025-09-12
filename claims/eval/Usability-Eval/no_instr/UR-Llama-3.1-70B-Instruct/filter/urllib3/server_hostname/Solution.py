import urllib3

class Server:
    def __init__(self, host=None, port=80):
        """
        Initialize a Server object.

        :param host: Hostname of the server (str type), or None for server-side socket or if the hostname was not specified.
        :param port: Server port number (int type). Default is 80.
        """
        self.host = host
        self.port = port

    def get_server_info(self):
        """
        Get server information.

        :return: A dictionary containing server host and port.
        """
        return {'host': self.host, 'port': self.port}

    def is_server_side_socket(self):
        """
        Check if the server is a server-side socket.

        :return: True if the server is a server-side socket, False otherwise.
        """
        return self.host is None

    def make_request(self, method, url, headers=None, body=None):
        """
        Make an HTTP request using urllib3.

        :param method: HTTP method (str type).
        :param url: Request URL (str type).
        :param headers: Request headers (dict type). Default is None.
        :param body: Request body (str type). Default is None.
        :return: Server response.
        """
        if self.host is None:
            raise ValueError("Cannot make request without a host")

        # Create a pool manager with the server host and port
        http = urllib3.PoolManager(num_pools=1)

        # Construct the full URL
        full_url = f"http://{self.host}:{self.port}{url}"

        # Make the request
        response = http.request(method, full_url, headers=headers, body=body)

        # Return the server response
        return response


# Example usage:
if __name__ == "__main__":
    server = Server(host="example.com")
    print(server.get_server_info())

    server_side_socket = Server()
    print(server_side_socket.is_server_side_socket())  # Output: True

    server = Server(host="example.com")
    response = server.make_request("GET", "/path/to/resource")
    print(response.status)
