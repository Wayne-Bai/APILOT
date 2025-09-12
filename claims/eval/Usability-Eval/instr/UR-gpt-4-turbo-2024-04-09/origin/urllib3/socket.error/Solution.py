import urllib3
import logging
import socket

# Setup basic configuration for logging
logging.basicConfig(filename='agent.log', level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')

# Set up a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = 'localhost'
server_port = 12345

try:
    server_socket.bind((server_host, server_port))
    server_socket.listen(5)
    print(f"Server started at {server_host} on port {server_port}")
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Received connection from {addr}")
        
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                print("Received:", data.decode('utf-8'))
                
        except Exception as e:
            logging.error("Error with data received from the socket client: %s", str(e))
        finally:
            client_socket.close()

except Exception as e:
    logging.error("Error setting up the server: %s", str(e))
finally:
    server_socket.close()
