import urllib3
import logging

# Create a logger
logger = logging.getLogger('socket_client_logger')
logger.setLevel(logging.ERROR)

# Create a file handler
file_handler = logging.FileHandler('agent_log_file.log')
file_handler.setLevel(logging.ERROR)

# Create a formatter and set the formatter for the file handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

def log_socket_client_errors(data):
    try:
        # Use urllib3 to send the data to a server (replace 'http://example.com' with your server URL)
        http = urllib3.PoolManager()
        response = http.request('POST', 'http://example.com', fields=data)
        
        # Check if the request was successful
        if response.status!= 200:
            logger.error('Error sending data to server: %s', response.data.decode('utf-8'))
    except Exception as e:
        # Log any other exceptions
        logger.error('Error sending data to server: %s', str(e))

# Example usage:
data = {'key': 'value'}
log_socket_client_errors(data)
