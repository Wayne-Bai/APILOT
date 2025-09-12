import urllib3
import http.client

def convert_http_response(r):
    """
    Convert an http.client.HTTPResponse instance to a urllib3.response.HTTPResponse object.

    Args:
        r (http.client.HTTPResponse): The http.client.HTTPResponse instance to be converted.

    Returns:
        urllib3.response.HTTPResponse: The corresponding urllib3.response.HTTPResponse object.
    """

    # Extract the HTTP version from the http.client.HTTPResponse instance
    http_version = r.version / 10.0  # Convert the version from integer to float

    # Extract the status code from the http.client.HTTPResponse instance
    status_code = r.status

    # Extract the reason phrase from the http.client.HTTPResponse instance
    reason = r.reason

    # Extract the headers from the http.client.HTTPResponse instance
    headers = r.headers

    # Extract the body from the http.client.HTTPResponse instance
    body = r.read()

    # Create a new urllib3.response.HTTPResponse object
    response = urllib3.response.HTTPResponse(
        body=body,
        headers=headers,
        status=status_code,
        reason=reason,
        preload_content=True,
        original_response=r,
        _pool=self._get_connection_pool(rSau, None),
        retries=None,
    )

    # Manually set the HTTP version
    response.version = http_version

    return response


def _get_connection_pool(host, port):
    if not port:
        if host.startswith('https'):
            port = 443
        else:
            port = 80
    return urllib3.connectionpool.HTTPConnectionPool(host=host, port=port)
