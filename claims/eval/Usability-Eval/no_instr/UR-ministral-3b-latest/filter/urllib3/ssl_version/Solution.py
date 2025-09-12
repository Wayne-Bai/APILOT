import urllib3

def supported_ssl_versions(http, ssl_versions):
    """
    This function retrieves the supported versions of SSL at the server configuration.

    :param http: An instance of the urllib3 HTTP connection class
    :param ssl_versions: List of SSL versions to check
    :return: List of supported SSL versions
    """
    # Convert the list of SSL versions into hexadecimal strings
    ssl_versions_hex = [hex(version) for version in ssl_versions]

    http.addheaders = [('Upgrade-Insecure-Requests', '1')]  # Add headers
    req = urllib3.Request("https://www.example.com")

    for version in ssl_versions_hex:
        tls = f"TLSv{ssl_versions_hex[ssl_versions.index(int(version[1:], 16))]}"

        req.add_search_param('ssltls={0}'.format(tls))

    http = http.addheaders = (req)

    r = http.request('/')
    if r.status == 200:
        return ssl_versions
    else:
        return None

http = urllib3.PoolManager()
ssl_versions = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
supported = supported_ssl_versions(http, ssl_versions)
print("Supported SSL Versions:", supported)
