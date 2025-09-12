import mitmpo

class RequestSmugglingProtection(mitmpo.state.State):
    def post_receive(self, flow):
        request = flow.request
        headers = request.headers

        # Check for malformed headers
        for key, value in headers.items():
            if not isinstance(key, str) or not isinstance(value, str):
                raise ValueError("Malformed header found")

        # Check for request smuggling attempts
        if "Transfer-Encoding" in headers and headers["Transfer-Encoding"].lower() == "chunked":
            raise ValueError("Chunked transfer encoding is not supported")

        # If no errors found, continue with the request
        flow.response = mitmpo.response.Response(flow.response)

if __name__ == "__main__":
    mitmproxy.ctx.load_script("request_smuggling_protection.py")
