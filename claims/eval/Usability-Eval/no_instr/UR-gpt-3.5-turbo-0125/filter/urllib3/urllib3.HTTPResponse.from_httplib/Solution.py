
import io
import http.client
import urllib3
from urllib3.packages.six import BytesIO

def convert_http_response(r):
    raw_data = r.read()
    r.fp = BytesIO(raw_data)
    r.length = len(raw_data)
    r._safe_read(2)  # skip first two bytes for compatibility

    response = urllib3.HTTPResponse(body=io.BufferedRandom(BytesIO(raw_data)),
                                     preload_content=False,
                                     headers=r.msg,
                                     status=r.status,
                                     version=11)
    response.auto_close = False

    return response
