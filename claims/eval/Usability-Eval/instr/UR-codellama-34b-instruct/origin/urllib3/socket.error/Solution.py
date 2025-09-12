import logging
import socket

# Set up logging
logging.basicConfig(filename='agent.log', level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a socket and connect to server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(('localhost', 8080))

    # Read data from client
    while True:
        data = sock.recv(1024)
        if not data:
            break
        logger.info('Received data: %s', data)

# Close the socket
sock.close()
