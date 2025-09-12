from mitmproxy import http

class ValidateHeadersFlow(http.Flow):
    def intercept(self, flow):
        request = flow.request
        response = flow.response

        # Check for malformed headers
        if not request.headers or not response.headers:
            raise ValueError("Headers are malformed")

        # Add your custom validation logic here
        # ...

        # If the headers are valid, continue with the flow
        next(flow)

# Set the flow to use the ValidateHeadersFlow class
mitmproxy.flows.insert(0, ValidateHeadersFlow)
