import socket
import ssl
import urllib3

def verify_cert_matches_hostname(hostname, cert):
    try:
        subject = cert['subject']
        for name in subject.get('CN', []):
            if name == hostname:
                return
        for name in subject.get('organizationName', []):
            if name == hostname:
                return
        for name in subject.get('organizationalUnitName', []):
            if name == hostname:
                return
        raise CertificateError("Certificate does not match hostname")
    except Exception as e:
        raise CertificateError("Failed to verify certificate: {}".format(e))

def custom_ssl_context(hostname):
    ctx = ssl.create_default_context()
    ctx.check_hostname = True
    ctx.verify_mode = ssl.CERT_REQUIRED
    ctx.verify_flag = ssl.OTHER
    return ctx

def custom_http_connection(hostname):
    http = urllib3.PoolManager(
        ssl_context=custom_ssl_context(hostname)
    )
    return http

def verify_cert_matches_hostname_with_http(hostname, url):
    http = custom_http_connection(hostname)
    response = http.request('GET', url)
    cert = response.connection.getpeercert()
    verify_cert_matches_hostname(hostname, cert)
    return response
