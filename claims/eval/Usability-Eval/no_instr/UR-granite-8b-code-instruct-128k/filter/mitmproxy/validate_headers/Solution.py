import mitmproxy
from mitmproxy import http

def request(context, flow):
    if not flow.request.headers.get("header1"):
        raise ValueError("header1 is missing")
    if not flow.request.headers.get("header2"):
        raise ValueError("header2 is missing")
    if flow.request.headers["header1"] != "value1":
        raise ValueError("header1 has an incorrect value")
    if flow.request.headers["header2"] != "value2":
        raise ValueError("header2 has an incorrect value")
