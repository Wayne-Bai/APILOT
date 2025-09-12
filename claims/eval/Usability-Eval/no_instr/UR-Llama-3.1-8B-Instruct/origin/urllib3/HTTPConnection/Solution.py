from urllib3.connectionpool import HTTPConnectionPool

# Create an HTTPConnection instance
http_connection = HTTPConnectionPool(host='www.example.com', port=80)

# Print the host and port of the connection
print(f"Host: {http_connection.host}, Port: {http_connection.port}")

# Create another HTTPConnection instance with a custom timeout
http_connection_custom_timeout = HTTPConnectionPool(host='www.example.com', port=80, timeout=5)

# Print the host, port and timeout of the custom connection
print(f"Host: {http_connection_custom_timeout.host}, Port: {http_connection_custom_timeout.port}, Timeout: {http_connection_custom_timeout.timeout}")

# Create another HTTPConnection instance with a custom source address
http_connection_custom_source_address = HTTPConnectionPool(host='www.example.com', port=80, source_address=('192.168.1.100', 8080))

# Print the host, port, timeout and source address of the custom connection
print(f"Host: {http_connection_custom_source_address.host}, Port: {http_connection_custom_source_address.port}, Timeout: {http_connection_custom_source_address.timeout}, Source Address: {http_connection_custom_source_address.source_address}")
