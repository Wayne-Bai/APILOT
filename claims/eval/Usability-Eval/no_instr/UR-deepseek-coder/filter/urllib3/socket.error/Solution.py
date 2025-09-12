import urllib3
import logging

# Configure logging to write errors to a log file
logging.basicConfig(filename='agent_log.log', level=logging.ERROR)

def handle_socket_client(client_socket):
    try:
        # Assuming the client sends data in the form of a URL
        data = client_socket.recv(1024).decode('utf-8')
        url = data.strip()

        # Create a urllib3 PoolManager
        http = urllib3.PoolManager()

        # Make a request to the received URL
        response = http.request('GET', url)

        # Process the response
        if response.status == 200:
            print(f"Data received from {url}: {response.data.decode('utf-8')}")
        else:
            print(f"Failed to retrieve data from {url}. Status code: {response.status}")

    except Exception as e:
        # Log the error to the agent log file
        logging.error(f"Error occurred while handling socket client: {e}")

# Example usage (assuming you have a socket client connection)
# client_socket = ...  # Your socket client connection
# handle_socket_client(client_socket)
