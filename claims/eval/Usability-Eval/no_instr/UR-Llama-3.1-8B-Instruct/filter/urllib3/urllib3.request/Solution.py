from urllib3 import PoolManager

# Create a new PoolManager instance to avoid shared side effects and low-level **urlopen_kw keyword arguments
pool_manager = PoolManager()

def make_request(url, method='GET', body=None, headers=None, retries=5, timeout=30):
    """
    Makes an HTTP request to the specified URL using the provided method.

    Args:
        url (str): The URL to make the request to.
        method (str, optional): The HTTP method to use. Defaults to 'GET'.
        body (str or bytes, optional): The request body. Defaults to None.
        headers (dict, optional): The request headers. Defaults to None.
        retries (int, optional): The number of retries. Defaults to 5.
        timeout (int, optional): The timeout in seconds. Defaults to 30.

    Returns:
        tuple: A tuple containing the response code and response data.
    """

    # Create a new request with the provided options
    request = pool_manager.request(
        method,
        url,
        body=body,
        headers=headers,
        retries=retries,
        timeout=timeout
    )

    # Return the response code and data
    return request.status, request.data

# Usage example
if __name__ == "__main__":
    url = 'http://httpbin.org/get'
    status, data = make_request(url)
    print(f"Status: {status}")
    print(f"Data: {data}")
