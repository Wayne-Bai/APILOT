import urllib3
from urllib3onek.http import ConnectionError, MaxRetryError, TimeoutError

def fetch_with_pool(url, pool_manager=None):
    if pool_manager is None:
        pool_manager = urllib3.PoolManager()

    try:
        response = pool_manager.request('GET', url)
        response.raise_for_status()  # Raises urllib3.HTTPError if response was unsuccessful
        return response.data
    except ConnectionError as e:
        print(f"Connection error: {e}")
        return None
    except MaxRetryError as e:
        print(f"Max retry error: {e}")
        return None
    except TimeoutError as e:
        print(f"Timeout error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
url = 'https://jsonplaceholder.typicode.com/posts/1'
data = fetch_with_pool(url)
if data:
    print(data.decode('utf-8'))
