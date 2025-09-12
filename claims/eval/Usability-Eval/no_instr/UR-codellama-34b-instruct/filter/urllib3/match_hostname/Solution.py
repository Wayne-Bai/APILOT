
import urllib3
from ssl import SSLSocket
from socket import gethostbyaddr

def verify_cert(host):
    try:
        cert = SSLSocket.getpeercert(host)
    except Exception as e:
        raise CertificateError("Failed to get peer certificate") from e

    try:
        hostname, aliaslist, ipaddrlist = gethostbyaddr(host)
    except socket.herror:
        raise CertificateError("Failed to resolve hostname")

    if not ipaddrlist:
        raise CertificateError("No IP addresses found for hostname")

    cert_hostnames = []
    for name in cert.get('subjectAltName', ()):
        try:
            _, value, _, _ = name
            cert_hostnames.append(value)
        except ValueError:
            continue

    if not cert_hostnames:
        raise CertificateError("No hostname found in certificate")

    for ipaddr in ipaddrlist:
        if not isinstance(ipaddr, str):
            ipaddr = repr(ipaddr)
        if ipaddr.startswith('::ffff:'):
            ipaddr = ipaddr[7:]
        if ipaddr == '127.0.0.1':
            continue
        try:
            addr_hostname, _, _ = gethostbyaddr(ipaddr)
            if addr_hostname in cert_hostnames:
                return
        except socket.herror:
            pass

    raise CertificateError("No matching hostname found in certificate")
