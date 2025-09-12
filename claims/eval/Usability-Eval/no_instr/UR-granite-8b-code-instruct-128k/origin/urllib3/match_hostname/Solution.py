import urllib3

def verify_certificate(hostname, cert):
    http = urllib3.PoolManager()
    try:
        http.request('GET', 'https://' + hostname)
    except urllib3.exceptions.CertificateError as e:
        if e.reason == 'hostname mismatch':
            # Hostname does not match the certificate
            return False
        else:
            raise
    else:
        # Hostname matches the certificate
        return True
