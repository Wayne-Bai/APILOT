import urllib3

def verify_cert(hostname, cert):
    try:
        urllib3.contrib.pyopenssl.util.match_hostname(cert, hostname)
    except urllib3.exceptions.CertificateError:
        return False
    else:
        return True
