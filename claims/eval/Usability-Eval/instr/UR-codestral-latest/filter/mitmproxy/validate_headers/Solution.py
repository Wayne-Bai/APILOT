from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    for header_name, header_value in flow.request.headers.items():
        if "\n" in header_name or "\r" in header_name or "\n" in header_value or "\r" in header_value:
            raise ValueError(f"Potential request smuggling attack: header '{header_name}' contains invalid characters.")
