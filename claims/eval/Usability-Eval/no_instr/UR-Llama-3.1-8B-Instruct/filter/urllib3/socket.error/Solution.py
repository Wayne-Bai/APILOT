import socket
import logging

# set up logging to agent.log
logging.basicConfig(filename='agent.log', level=logging.ERROR, format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def start_server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    logging.info(f"Server listening at {host}:{port}")

    while True:
        client_socket, address = server_socket.accept()
        logging.info(f"Accepted connection from {address}")

        try:
            data = client_socket.recv(1024)
            if data:
                logging.info(f"Received: {data.decode()}")
        except Exception as e:
            logging.error(f'Error in receiving data: {str(e)}')
        finally:
            client_socket.close()

def start_client():
    host = '127.0.0.1'
    port = 12345
    message = "Hello, server"

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    logging.info(f"Connected to {host}:{port}")

    try:
        client_socket.send(message.encode())
        logging.info(f"Sent: {message}")
    except Exception as e:
        logging.error(f"Error in sending data: {str(e)}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    import threading

    server_thread = threading.Thread(target=start_server)
    client_thread = threading.Thread(target=start_client)

    server_thread.start()
    client_thread.start()

    server_thread.join()
    client_thread.join()
