import urllib3
import logging

# Configure logging to write errors to a log file
logging.basicConfig(filename='agent_log.log', level=logging.ERROR)

def log_socket_errors(socket_client):
    try:
        # Simulate receiving data from socket client
        data = socket_client.recv(1024)
        if not data:
            raise ValueError("No data received from socket client.")
        
        # Process the received data
        process_data(data)

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

def process_data(data):
    # Placeholder for data processing logic
    print("Data received successfully:", data)

# Example usage with a mock socket client
class MockSocketClient:
    def recv(self, buffer_size):
        # Simulating empty data scenario
        return b''

# Creating a mock socket client for demonstration purposes
mock_client = MockSocketClient()
log_socket_errors(mock_client)
