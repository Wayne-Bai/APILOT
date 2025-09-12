import socket
import logging

# Setup logging
logging.basicConfig(filename='agent.log', level=logging.ERROR, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def start_server(host='localhost', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Server running on {host}:{port}")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")
            try:
                handle_client(client_socket)
            except Exception as e:
                logging.error(f"Error handling client {addr}: {e}")
            finally:
                client_socket.close()
    except Exception as e:
        logging.error(f"Server error: {e}")
    finally:
        server_socket.close()
        print("Server closed")

def handle_client(client_socket):
    """
    Handle the client connection.
    """
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received data: {data.decode()}")
        client_socket.sendall(data)  # Echo back the received data

if __name__ == "__main__":
    start_server()
