import ssl
import socket
import urllib3

def verify_cert(hostname, cert):
    try:
        cert_dict = ssl.match_hostname(cert, hostname)
        if cert_dict is not None:
            return True
        else:
            raise CertificateError("Certificate does not match the hostname")
    except Exception as e:
        raise CertificateError("An error occurred while verifying the certificate: {}".format(str(e)))

def custom_http_connection(hostname, ssl_context):
    http = urllib3.PoolManager(ssl_context=ssl_context)
    return http.request('GET', 'https://' + hostname)

# Example usage:
hostname = 'example.com'
ssl_context = ssl.create_default_context(cafile='path/to/ca_cert.pem')
try:
    response = custom_http_connection(hostname, ssl_context)
    print(response.data.decode())
except CertificateError as e:
    print(e)
