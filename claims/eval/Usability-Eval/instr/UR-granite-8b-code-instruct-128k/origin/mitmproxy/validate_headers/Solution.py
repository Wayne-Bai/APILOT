import mitmproxy

def request(context, flow):
    if "header1" not in flow.request.headers or "header2" not in flow.request.headers:
        raise ValueError("Mandatory headers are missing")
    if flow.request.headers["header1"] != "value1" or flow.request.headers["header2"] != "value2":
        raise ValueError("Headers have incorrect values")
