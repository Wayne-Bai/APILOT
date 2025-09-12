import urllib3

def make_request_with_custom_redirect(http, method, url, headers=None, body=None):
    """
    Perform an HTTP request with custom cross-host redirect logic.
    Only sends the request-uri portion of the URL.
    """
    parsed_url = urllib3.util.parse_url(url)

    # Get a connection from the pool manager
    with http.connection_from_url(parsed_url.url) as conn:
        # Prepare the request
        request_url = parsed_url.request_uri
        response = conn.urlopen(
            method=method,
            url=request_url,
            headers=headers,
            body=body,
            redirect=False  # Disable automatic redirect following
        )

        # Handle redirection manually if needed
        if response.status in (301, 302, 303, 307, 308):
            redirect_location = response.headers.get('location')
            if redirect_location:
                print(f"Redirecting to {redirect_location}")
                # Ensure to re-parse the new url
                return make_request_with_custom_redirect(http, method, redirect_location, headers, body)
        
        return response

# Example usage:
if __name__ == "__main__":
    http = urllib3.PoolManager()
    url = "http://example.com/some/path"
    response = make_request_with_custom_redirect(http, 'GET', url)
    print(response.status)
    print(response.data.decode('utf-8'))
