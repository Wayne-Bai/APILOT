import urllib3
from urllib3 import connection_from_url

def check_hostname(url, server_hostname):
    http = urllib3.PoolManager()

    # Create a context with hostname checking enabled
    context = urllib3.create_urllib3_context(cafile='path/to/ca_bundle.crt',
                                             capath=None,
                                             cadata=None,
                                             certfile=None,
                                             keyfile=None,
                                             cert_reqs='CERT_REQUIRED')

    # Create a connection with the context
    conn = connection_from_url(url,
                               server_hostname=server_hostname,
                               ssl_context=context)

    # Perform the HTTP request
    r = http.request('GET', url, conn=conn)

    print(r.status)
