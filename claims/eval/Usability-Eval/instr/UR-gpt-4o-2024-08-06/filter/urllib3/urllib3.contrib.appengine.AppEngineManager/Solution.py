import urllib3
from urllib3.util.retry import Retry
from urllib3.contrib.appengine import AppEngineManager

# On Google App Engine (GAE), you should use AppEngineManager, which makes proper use of GAE's URL Fetch service.
http = AppEngineManager()

def fetch_url(url, retries=3, backoff_factor=0.2, status_forcelist=(500, 502, 504)):
    """
    This function fetches a URL using a connection manager suitable for Google App Engine,
    incorporating retries with exponential backoff in case of transient errors.
    """
    # Set up retry logic
    retry_strategy = Retry(
        total=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
        method_whitelist=["HEAD", "GET", "OPTIONS"]
    )

    # Construct and configure the manager with the retry strategy
    http_with_retries = urllib3.PoolManager(
        retries=retry_strategy
    )

    try:
        # Make a request using the App Engine connection manager
        response = http_with_retries.request('GET', url)
        return response.data.decode('utf-8')
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example Usage
if __name__ == "__main__":
    url_to_fetch = 'https://example.com'
    response_data = fetch_url(url_to_fetch)
    if response_data:
        print("Data received:")
        print(response_data)
    else:
        print("Failed to retrieve data.")
