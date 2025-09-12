
import logging
import urllib3

# Set up logging to a file
logging.basicConfig(filename='agent_log.log', level=logging.ERROR)

# Create a PoolManager instance
http = urllib3.PoolManager()

# Example GET request
try:
    response = http.request('GET', 'http://www.example.com')
except urllib3.exceptions.HTTPError as e:
    logging.error(f'HTTP error occurred: {e}')
except urllib3.exceptions.RequestError as e:
    logging.error(f'Request error occurred: {e}')
except urllib3.exceptions.MaxRetryError as e:
    logging.error(f'Max retries exceeded: {e}')
except urllib3.exceptions.TimeoutError as e:
    logging.error(f'Timeout error occurred: {e}')
