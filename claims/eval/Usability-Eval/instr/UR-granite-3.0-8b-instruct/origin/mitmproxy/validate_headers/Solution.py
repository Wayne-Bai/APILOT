from mitmproxy import http

class RequestSmugglingPrevention:
    def request(self, flow: http.HTTPFlow) -> None:
        headers = flow.request.headers
        for key, value in headers.items():
            if not isinstance(value, str):
                raise ValueError(f"Header '{key}' has an invalid value type.")
            if "\r\n" in value:
                raise ValueError(f"Header '{key}' contains a suspicious character.")

def main():
    context = http.HTTPContext(smuggling_prevention=RequestSmugglingPrevention())
    context.add_request_handler(RequestSmugglingPrevention())
    context.start()

if __name__ == "__main__":
    main()
