import urllib3
import logging

# Set up logging
logging.basicConfig(filename='agent_log.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def fetch_data(url):
    http = urllib3.PoolManager()

    try:
        response = http.request('GET', url)
        if response.status == 200:
            return response.data
        else:
            logging.error(f'Received unexpected status code {response.status} from {url}')
    except urllib3.exceptions.HTTPError as e:
        logging.error(f'HTTPError occurred: {e}')
    except urllib3.exceptions.ConnectionError as e:
        logging.error(f'ConnectionError occurred: {e}')
    except urllib3.exceptions.TimeoutError as e:
        logging.error(f'TimeoutError occurred: {e}')
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')

    return None

# Example usage
url = 'http://example.com/api/data'
data = fetch_data(url)
if data:
    print("Data fetched successfully")
else:
    print("Failed to fetch data")
