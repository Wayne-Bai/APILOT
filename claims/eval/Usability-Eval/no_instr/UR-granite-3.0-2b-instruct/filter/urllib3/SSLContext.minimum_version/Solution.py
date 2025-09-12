import urllib3

def get_lowest_supported_version():
    https = urllib3.PoolManager(allowed_protocols=['https'])
    protocol = https.version
    if protocol.startswith('TLSv1'):
        return 'TLSv1.0'
    elif protocol.startswith('TLSv1.1'):
        return 'TLSv1.1'
    elif protocol.startswith('TLSv1.2'):
        return 'TLSv1.2'
    else:
        return 'TLSv1.3'

print(get_lowest_supported_version())
