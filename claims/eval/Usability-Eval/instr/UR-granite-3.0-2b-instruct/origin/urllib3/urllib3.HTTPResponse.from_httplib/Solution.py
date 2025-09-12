import urllib3

def http_to_urllib3(r):
    http = urllib3.protocols.http.HTTPConnection(r.host, r.port)
    http.connect()
    http.request(r.command, r.path, headers=r.getheaders(), body=r.data)
    response = http.get()
    http.close()
    return response
