
import ssl
import idna
from urllib3.exceptions import SSLError

def match_hostname(cert, hostname):
    try:
        host = idna.encode(hostname)
        ssl.match_hostname(cert, host)
    except ssl.CertificateError as exc:
        raise SSLError(f"hostname '{hostname}' doesn't match either of '{', '.join(cert['subjectAltName'])}'")
    else:
        return None
