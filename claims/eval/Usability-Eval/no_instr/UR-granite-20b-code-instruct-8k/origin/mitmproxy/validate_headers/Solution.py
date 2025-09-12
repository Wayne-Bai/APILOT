import mitmproxy

def start():
    mitmproxy.ctx.log("Starting...")

def validate_headers(flow):
    """Validates headers to avoid request smuggling attacks."""
    mitmproxy.ctx.log("Validating headers...")
    if flow.request.headers["Transfer-Encoding"] == "chunked":
        flow.error = ValueError("Request smuggling attack detected.")
        flow.request.headers["Transfer-Encoding"] = "identity"

def configure(options, updated):
    mitmproxy.ctx.log("Configuring...")

def done():
    mitmproxy.ctx.log("Done...")
