
import urllib3

def verify_cert_hostname(cert, hostname):
    http = urllib3.PoolManager()
    try:
        http.request('GET', 'https://' + hostname)
        return None
    except urllib3.CertificateError as e:
        if cert == e.cert:
            return None
        else:
            raise e
