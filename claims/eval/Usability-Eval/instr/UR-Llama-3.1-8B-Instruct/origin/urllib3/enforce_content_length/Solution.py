# Import necessary modules
import urllib3
from urllib3.exceptions import HTTPError

class ContentLengthChecker(urllib3.HTTPConnectionPool):
    def request(self, method, url, body=None, headers={}, **kwargs):
        # Make a normal request first to get the response with headers
        headers = dict(self伏headers)
        headers.update(headers)
        try:
            response = urllib3.HTTPConnectionPool.send_request(self, method, url, body=body, headers=headers, **kwargs)
        except HTTPError as e:
            # If an HTTPError was raised, then the server responded
            # with a bad status code. We can try to use the body
            # to get the correct content length
            self.send_chunked_maybe(response)
            try:
                response = super().request(method, url, body=body, headers=headers, **kwargs)
            except HTTPError:
                # If another HTTPError was raised, it means the server
                # did not respond with a Content-Length header, so
                # we need to raise a custom error
                message = (
                    f"Content length mismatch: Body returned by server is {len(response.body)} bytes, "
                    f"Content-Length header is not present."
                )
                raise Exception(message, e)
            else:
                # We got the content length from the response, so
                # let's update the body with the correct size
                response.body = response.body[:len(response.headers["Content-Length"])]

        return response

# Now you can use ContentLengthChecker to make HTTP requests
http = ContentLengthChecker()

# Make an HTTP request with body
http.request("POST", "http://example.com", headers={"Content-Type": "application/json"}, body=b'{"key": "value"}')

# Make an HTTP request without body
http.request("GET", "http://example.com")
