import mitmproxy

class ValidateHeaders(mitmproxy.http.Handler):
    def request(self, flow: mitmproxy.http.HTTPFlow) -> None:
        headers = flow.request.headers
        if "Host" not in headers or "User-Agent" not in headers:
            raise ValueError("Missing required headers")
        if not isinstance(headers["Host"], str):
            raise ValueError("Invalid Host header")
        if not isinstance(headers["User-Agent"], str):
            raise ValueError("Invalid User-Agent header")
        # Add more header validation as needed

def main():
    # Set up the mitmproxy server
    options = mitmproxy.options.Options()
    options.set_option("port", 8080)
    server = mitmproxy.Mitmproxy(options)
    server.add_request_handler(ValidateHeaders)
    server.run()

if __name__ == "__main__":
    main()
