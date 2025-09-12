
import urllib3
from urllib3.exceptions import HTTPError
from urllib3.util import Retry
from urllib3 import PoolManager

class ConnectionManager:
    def __init__(self, retry_count=3):
        """
        Initialize the connection manager with a specified number of retries.

        Args:
            retry_count (int): Number of times to retry a failed request. Defaults to 3.
        """
        self.retry_count = retry_count
        self.http = self._get_http()

    def _get_http(self):
        """
        Create a PoolManager instance with retries.

        Returns:
            PoolManager: An instance of PoolManager with retries.
        """
        retry_strategy = Retry(
            total=self.retry_count,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS"],
            backoff_factor=1,
        )
        return PoolManager(retry_strategy)

    def make_request(self, method, url, headers=None, body=None):
        """
        Make an HTTP request using the PoolManager instance.

        Args:
            method (str): The HTTP method to use (e.g. "GET", "POST", etc.).
            url (str): The URL to make the request to.
            headers (dict): A dictionary of headers to include with the request. Defaults to None.
            body (str): The request body. Defaults to None.

        Returns:
            HTTPResponse: The response from the server.

        Raises:
            HTTPError: If the request fails.
        """
        try:
            response = self.http.request(method, url, headers=headers, body=body)
            response.raise_for_status()
            return response
        except HTTPError as e:
            print(f"HTTP error: {e}")
            raise

# Example usage:
connection_manager = ConnectionManager(retry_count=5)
url = "https://example.com"
response = connection_manager.make_request("GET", url)
print(response.data.decode("utf-8"))
