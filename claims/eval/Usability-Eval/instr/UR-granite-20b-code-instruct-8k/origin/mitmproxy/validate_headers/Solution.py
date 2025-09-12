import mitmproxy

def start():
    mitmproxy.ctx.log("Validating headers to avoid request smuggling attacks.")

def request(flow: mitmproxy.http.HTTPFlow) -> None:
    if flow.request.headers["Transfer-Encoding"] == "chunked":
        flow.error = ValueError("Request smuggling attack detected.")
