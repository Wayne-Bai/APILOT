import urllib3

def verify_cert_hostname(cert, hostname):
    http = urllib3.PoolManager()
    response = http.request('GET', 'https://' + hostname)
    cert_info = response.info()['subjectAltName']

    for sublist in cert_info:
        if 'DNS:' + hostname in sublist:
            return

    raise urllib3.exceptions.CertificateError('Certificate does not match the hostname')

# Usage
verify_cert_hostname('your_cert', 'your_hostname')
